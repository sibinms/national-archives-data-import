from django.core.management import BaseCommand

from archive_records.models import ArchiveRecord
from archive_records.utils import get_record_from_national_archives, format_and_save_record_to_database


class Command(BaseCommand):
    """
    Management command to import a record from the National Archives
    http://discovery.nationalarchives.gov.uk/API/sandbox/index
    """
    help = "Management command to import a record from the National Archives"

    def add_arguments(self, parser):
        parser.add_argument(
            'record_id',
            type=str,
            help='Record ID for fetching the data'
        )

    def handle(self, *args, **kwargs):
        record_id = kwargs['record_id']

        is_record_exists = self.check_record_already_exists(record_id)
        if is_record_exists:
            self.stdout.write("Record already exist in the DB")
            return

        response = get_record_from_national_archives(record_id)
        if response.status_code == 204:
            self.stdout.write("No record found")
            return

        if response.status_code == 200:
            format_and_save_record_to_database(
                response
            )
            self.stdout.write("Record found and saved to the DB")
            return

        self.stdout.write(f"Something unexpected happened{response.status_code}")
        return

    @staticmethod
    def check_record_already_exists(record_id):
        return ArchiveRecord.objects.filter(
            reference_id=record_id
        ).exists()

