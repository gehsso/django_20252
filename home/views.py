from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Página Principal Novo Teste</h1>')

def sobre(request):
    return HttpResponse('Sobre o Sistema Django!')

def contato(request):
    return HttpResponse('Contato')

def ajuda(request):
    return HttpResponse('ajuda')