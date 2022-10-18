from django.db import models

# Create your models here.


class ArchiveRecord(models.Model):
    reference_id = models.CharField(max_length=250, unique=True)
    title = models.CharField(null=True, blank=True, max_length=250)
    description = models.TextField(null=True, blank=True)
    citable_reference = models.CharField(null=True, blank=True, max_length=250)

    def get_display_message(self):
        message = "Not sufficient information"

        if self.title:
            message = f"Title : {self.title}"
            return message

        if self.description:
            message = f"Description : {self.description}"
            return message

        if self.citable_reference:
            message = f"Citable reference: {self.citable_reference}"
            return message

        return message

