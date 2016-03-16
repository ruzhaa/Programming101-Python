from django.conf.urls import url
# from django.contrib import admin

from .views import *


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^course/new$', create_new_course, name='create_new_course'),
    url(r'^course/edit/', edit_course, name='edit_course'),
    url(r'^lecture/new$', create_lecture, name='create_lecture'),
    url(r'^lecture/edit', create_lecture, name='create_lecture'),

    # url(r'^', go_to_course, name='go_to_course'),

]
