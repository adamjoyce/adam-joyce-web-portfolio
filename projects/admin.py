from django.contrib import admin

from.models import FinancialCategory, TechnologyCategory, Project

admin.site.register(Project)
admin.site.register(FinancialCategory)
admin.site.register(TechnologyCategory)
