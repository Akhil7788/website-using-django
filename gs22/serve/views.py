from django.shortcuts import render

# Create your views here.4

def services(request):
    return render(request, 'serv/services.html')