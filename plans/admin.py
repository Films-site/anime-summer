from django.contrib import admin

from plans.models import Plan, PlanItem


@admin.register(Plan)
class PlanModelAdmin(admin.ModelAdmin):
    ...


@admin.register(PlanItem)
class PlanItemModelAdmin(admin.ModelAdmin):
    ...
