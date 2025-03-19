from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('finances/', include('finances.urls')),
    path('users/', include('users.urls')),
    path('integrations/', include('integrations.urls')),
    path('notifications/', include('notifications.urls')),
    path('reports/', include('reports.urls')),
    path('goals/', include('goals.urls')),
    path('analytics/', include('analytics.urls')),
]