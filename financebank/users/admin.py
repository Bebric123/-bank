from django.contrib import admin
from finances.models import FinanceRecord
from goals.models import FinancialGoal
from analytics.models import Analytics
from notifications.models import Notification
from reports.models import Report
from integrations.models import CSVImport



admin.site.register(FinanceRecord)
admin.site.register(FinancialGoal)
admin.site.register(Analytics)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(CSVImport)