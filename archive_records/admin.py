from django.contrib import admin

# Register your models here.
from archive_records.models import ArchiveRecord


@admin.register(ArchiveRecord)
class ArchiveRecordAdminView(admin.ModelAdmin):
    list_display = ('reference_id', 'title')
    search_fields = ('reference_id', 'title')
