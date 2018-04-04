from django.contrib import admin

from .models import Club_info, Club_member, Core_team, Club_budget, Session_info, Club_report, Fest_budget, Other_report, Change_office

# Register your models here.

admin.site.register(Club_info)
admin.site.register(Club_member)
admin.site.register(Core_team)
admin.site.register(Club_budget)
admin.site.register(Session_info)
admin.site.register(Club_report)
admin.site.register(Fest_budget)
admin.site.register(Other_report)
admin.site.register(Change_office)
