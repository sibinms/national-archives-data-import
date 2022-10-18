import requests

from archive_records.models import ArchiveRecord


def get_record_from_national_archives(record_id):
    response = requests.get(
        url=f"http://discovery.nationalarchives.gov.uk/API/records/v1/details/{record_id}"
    )
    return response


def format_and_save_record_to_database(response):
    try:
        record = response.json()
        record_id = record['id']
        record_title = record.get('title', '')
        scope_content = record.get('scopeContent', {})
        description = scope_content.get('description', "")
        citable_reference = record.get('citableReference', "")

        archive_record = ArchiveRecord(
            reference_id=record_id,
            title=record_title,
            description=description,
            citable_reference=citable_reference
        )
        archive_record.save()
        return True

    except Exception:
        return False
