from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})


def factorialContainer(request):
    if request.method == 'POST':
        input_numer = int(request.POST.get('factoriel'))
        factoriel = 1
        while input_numer != 1:
            factoriel *= input_numer
            input_numer -= 1
        fact_result = factoriel
    return render(request, 'index.html', locals())


def fibonacciContainer(request):
    if request.method == 'POST':
        input_numer = int(request.POST.get('fibonacci'))
        fib_result = ""
        a, b = 1, 1
        for n in range(1, input_numer):
            fib_result += str(a)
            a, b = b, a + b
    return render(request, 'index.html', locals())


def primesContainer(request):
    if request.method == 'POST':
        input_numer = int(request.POST.get('primes'))
        # prime_result
    return render(request, 'index.html', locals())


def encodeContainer(request):
    if request.method == 'POST':
        encode_input = int(request.POST.get('encode'))
        #  encode_result
    return render(request, 'index.html', locals())


def decodeContainer(request):
    if request.method == 'POST':
        decode_input = int(request.POST.get('decode'))
        # decode_result
    return render(request, 'index.html', locals())
