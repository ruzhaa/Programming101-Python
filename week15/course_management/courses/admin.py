from django.contrib import admin
from .models import Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "start_date", "end_date")


admin.site.register(Courses, CoursesAdmin)
