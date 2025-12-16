from django.contrib import admin
from .models import *
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "is_completed", "updated_at")


admin.site.register(Task, TaskAdmin)
