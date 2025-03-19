from django.contrib import admin
from .models import Profile, Category, Transaction, FinancialGoal, Notification, Report

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(FinancialGoal)
admin.site.register(Notification)
admin.site.register(Report)