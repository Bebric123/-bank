from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import FinancialGoal

@receiver(post_save, sender=FinancialGoal)
def check_goal_progress(sender, instance, **kwargs):
    progress = instance.progress()
    notification_thresholds = [50, 75, 100] 

    for threshold in notification_thresholds:
        if progress >= threshold and instance.notified_progress < threshold:
            send_mail(
                subject=f"Вы достигли {threshold}% вашей цели!",
                message=f"Поздравляем! Вы достигли {threshold}% от своей цели: {instance.title}. Продолжайте в том же духе!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.user.email],
                fail_silently=True,
            )
            instance.notified_progress = threshold
            instance.save(update_fields=["notified_progress"])
            break