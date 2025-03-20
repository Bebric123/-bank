from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название цели")
    target_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Целевая сумма")
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Текущая сумма")
    deadline = models.DateField(verbose_name="Срок достижения")
    created_at = models.DateTimeField(auto_now_add=True)

    def progress(self):
        return (self.current_amount / self.target_amount) * 100 if self.target_amount > 0 else 0

    def __str__(self):
        return f"{self.title} - {self.current_amount}/{self.target_amount}"