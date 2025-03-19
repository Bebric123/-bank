from django.db import models

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)
    generated_at = models.DateTimeField(auto_now_add=True)
    report_data = models.TextField()