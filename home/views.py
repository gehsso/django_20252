from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Página Principal</h1>')

def sobre(request):
    return HttpResponse('Sobre o Sistema Django')
