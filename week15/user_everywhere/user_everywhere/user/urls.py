from django.conf.urls import url

from .views import home, register, login, profile
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register$', register, name='register'),
    url(r'^login$', login, name='login'),
    url(r'^profile$', profile, name='profile'),
    # url(r'^logout$', logout, name='logout'),
]
