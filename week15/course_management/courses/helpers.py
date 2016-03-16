from datetime import datetime


def diff_month(d1, d2):
    parsed_start = datetime.strptime(d2, "%Y-%m-%d")
    parsed_end = datetime.strptime(d1, "%Y-%m-%d")
    return (parsed_end.year - parsed_start.year)*12 + parsed_end.month - parsed_start.month


def get_post_attr(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    approximate = diff_month(end_date, start_date)

    return name, description, start_date, end_date, approximate


def get_post_attr_lecture(request):
    lecture = request.POST.get('lecture')
    week = request.POST.get('week')
    course = request.POST.get('course')
    URL = request.POST.get('URL')

    return lecture, week, course, URL
