from django.contrib import admin
from .models import Courses, Lectures


class CoursesAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "description",
                    "start_date",
                    "end_date",
                    "approximate")


class LecturesAdmin(admin.ModelAdmin):
    list_display = ("unique_id",
                    "lecture",
                    "week",
                    "course",
                    "URL")


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Lectures, LecturesAdmin)
