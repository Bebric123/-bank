from django.core.mail import send_mail
from django.conf import settings
from .models import FinancialGoal

def update_goal_progress(user, amount, goal_id):
    try:
        goal = FinancialGoal.objects.get(id=goal_id, user=user)
        goal.saved_amount += amount
        goal.save()

        progress = goal.progress_percentage()
        subject = "Прогресс вашей финансовой цели"
        message = f"Вы на {progress}% ближе к своей цели «{goal.name}»!"

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return f"Прогресс обновлен: {progress}%"

    except FinancialGoal.DoesNotExist:
        return "Цель не найдена"