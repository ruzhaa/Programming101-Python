from django.shortcuts import render
from .models import Courses

# Create your views here.


def home(request):
    return render(request, 'index.html', locals())


def go_to_course(request):
    if request.GET.get('name'):
        post = Courses.objects.filter('name')
    return render(request, 'python.html', locals())


def create_new_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        # print(description)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        a = Courses(name=name,
                    description=description,
                    start_date=start_date,
                    end_date=end_date)
        a.save()

    return render(request, 'form.html', locals())
