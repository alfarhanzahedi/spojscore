from django.contrib import admin

from .models import Problem

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass
