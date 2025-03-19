from django.db import models

class CSVImport(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CSV {self.file.name} ({self.uploaded_at})"