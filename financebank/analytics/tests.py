from finances.models import FinanceRecord
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model() 

class FinanceAnalyticsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        FinanceRecord.objects.create(user=self.user, transaction_type="income", category="Salary", amount=5000, date=date.today())
        FinanceRecord.objects.create(user=self.user, transaction_type="expense", category="Food", amount=2000, date=date.today())
        self.client.login(username="testuser", password="testpass")

    def test_balance_calculation(self):
        response = self.client.get(reverse("analytics"))
        self.assertContains(response, "Общий доход:")
        self.assertContains(response, "Общие расходы:")