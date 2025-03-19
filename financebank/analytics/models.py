from django.db import models

# Create your models here.
class Analytics(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    analysis_date = models.DateTimeField(auto_now_add=True)