from django.shortcuts import render

from .models import Courses, Lectures
from .helpers import get_post_attr, get_post_attr_lecture


def home(request):
    list_with_fields = []

    for elem in Courses.objects.all():
        list_with_fields.append(elem)

    return render(request, 'course_table.html', locals())


def create_new_course(request):
    if request.method == 'POST':
        name, description, start_date, end_date, approximate = get_post_attr(request)

        a = Courses(name=name,
                    description=description,
                    start_date=start_date,
                    end_date=end_date,
                    approximate=approximate)

        a.save()
    return render(request, 'form.html', locals())


def edit_course(request):
    course_name_for_edit = request.path.split('/')[-1]

    if request.method == 'GET':
        course = Courses.objects.get(name=course_name_for_edit)
        return render(request, 'edit_course.html', locals())

    if request.method == 'POST':
        name, description, start_date, end_date, approximate = get_post_attr(request)

        a = Courses.objects.filter(name=course_name_for_edit)\
                           .update(name=name,
                                   description=description,
                                   start_date=start_date,
                                   end_date=end_date,
                                   approximate=approximate)
        return home(request)


def create_lecture(request):
    if request.method == 'GET':
        return render(request, 'new_lecture.html', locals())

    if request.method == 'POST':
        lecture, week, course, URL = get_post_attr_lecture(request)
        course = request.POST.get("course")

        if course == Courses.objects.get(name=course).name:

            l = Lectures(lecture=lecture,
                         week=week,
                         course=Courses.objects.get(name=course),
                         URL=URL)
            l.save()
            return render(request, 'index.html', locals())
