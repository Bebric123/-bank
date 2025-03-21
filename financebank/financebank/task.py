from celery import shared_task
from notifications.utils import send_email_notification
from django.contrib.auth import get_user_model

@shared_task
def daily_expense_reminder():
    User = get_user_model()
    users = User.objects.all()
    for user in users:
        send_email_notification(
            user.email,
            "Ежедневное напоминание",
            "Не забудьте внести свои расходы за сегодня!"
        )