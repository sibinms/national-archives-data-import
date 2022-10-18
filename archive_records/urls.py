from django.urls import path

from archive_records.views import ArchiveRecordsView

app_name = 'archive_records'

urlpatterns = [
    path('archive-records/', ArchiveRecordsView.as_view(), name='archive-records'),
]
