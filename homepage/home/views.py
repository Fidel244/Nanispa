from django.shortcuts import render
# Create your views here.

def mostrar_homepage(request):
    return render(request, 'index.html')
