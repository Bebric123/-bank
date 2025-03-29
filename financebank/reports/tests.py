from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from finances.models import FinanceRecord
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model() 

class ExportCSVTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        FinanceRecord.objects.create(user=self.user, transaction_type="income", category="Salary", amount=5000, date=date.today())

    def test_export_csv(self):
        response = self.client.get(reverse("export_csv"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")
        self.assertIn("Salary", response.content.decode())