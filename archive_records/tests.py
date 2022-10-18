from django.db import IntegrityError
from django.test import TestCase
from archive_records.models import ArchiveRecord


class ArchiveRecordsViewTestCase(TestCase):
    def test_url_available(self):
        response = self.client.get('/archive-records/')
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get('/archive-records/')
        self.assertTemplateUsed(response, "national_archives/records.html")

    def test_template_content(self):
        response = self.client.get('/archive-records/')
        self.assertContains(response, "<h1>Fetch the record</h1>")
        self.assertNotContains(response, "Not on the page")


class ArchiveRecordTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.archive_record = ArchiveRecord.objects.create(
            reference_id="reference_id",
            title="title",
            description="description",
            citable_reference="citable_reference"
        )

    def test_model_content(self):
        self.assertEqual(self.archive_record.reference_id, "reference_id")
        self.assertEqual(self.archive_record.title, "title")
        self.assertEqual(self.archive_record.description, "description")
        self.assertEqual(self.archive_record.citable_reference, "citable_reference")

    def test_uniqueness(self):
        with self.assertRaises(IntegrityError):
            ArchiveRecord.objects.create(reference_id='reference_id')

    def test_model_function_get_display_message(self):
        self.assertEqual(
            self.archive_record.get_display_message(), f"Title : {self.archive_record.title}"
        )
