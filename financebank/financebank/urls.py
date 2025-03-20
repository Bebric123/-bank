from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_dashboard(request):
    return redirect("users/")  # Перенаправление на главную страницу

urlpatterns = [
    path("admin/", admin.site.urls),
    path("finances/", include("finances.urls")),
    path("users/", include("users.urls")),
    path("integrations/", include("integrations.urls")),
    path("notifications/", include("notifications.urls")),
    path("reports/", include("reports.urls")),
    path("goals/", include("goals.urls")),
    path("analytics/", include("analytics.urls")),

    path("", redirect_to_dashboard),  # Теперь `/` перенаправит на `dashboard`
]
