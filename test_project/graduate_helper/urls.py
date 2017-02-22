from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^factoriel$', views.factorialContainer, name='factorial_container'),
    url(r'^fibonacci$', views.fibonacciContainer, name='fibonacci_container'),
    url(r'^primes$', views.primesContainer, name='primes_container'),
    url(r'^encode$', views.encodeContainer, name='encode_container'),
    url(r'^decode$', views.decodeContainer, name='decode_container'),
]
