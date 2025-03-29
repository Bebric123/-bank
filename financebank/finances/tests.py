from django.test import TestCase
from finances.models import FinanceRecord
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model() 

class FinanceRecordModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_create_finance_record(self):
        record = FinanceRecord.objects.create(
            user=self.user,
            transaction_type="income",
            category="Зарплата",
            amount=5000.00,
            date=date.today()
        )
        self.assertEqual(record.user.username, "testuser")
        self.assertEqual(record.transaction_type, "income")
        self.assertEqual(record.amount, 5000.00)