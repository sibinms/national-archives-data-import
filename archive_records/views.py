from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.views import generic

from archive_records.models import ArchiveRecord


class ArchiveRecordsView(generic.TemplateView):
    template_name = "national_archives/records.html"
    message = None

    def get_context_data(self, **kwargs):
        context = super(ArchiveRecordsView, self).get_context_data(**kwargs)
        record_id = self.request.GET.get("record_id", None)
        if record_id:
            self.get_display_message(record_id)
            context.update({
                "message": self.message
            })

        return context

    def get_display_message(self, record_id):
        try:
            archive_record = ArchiveRecord.objects.get(
                reference_id=record_id
            )
            self.message = archive_record.get_display_message()
        except ObjectDoesNotExist:
            self.message = "No record found"
