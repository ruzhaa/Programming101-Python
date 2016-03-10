from django.conf.urls import url
# from django.contrib import admin

from .views import home, go_to_course, create_new_course


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^new/', create_new_course, name='create_new_course'),
    url(r'^', go_to_course, name='go_to_course'),

]
