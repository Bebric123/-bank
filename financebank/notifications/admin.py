from django.contrib import admin
from .models import FinanceRecord, FinancialGoal, Analytics, Notification, Report, CSVImport


admin.site.register(FinanceRecord)
admin.site.register(FinancialGoal)
admin.site.register(Analytics)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(CSVImport)