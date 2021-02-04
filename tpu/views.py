from django.shortcuts import render
from django.http import HttpResponse
from .models import building

from django.http import HttpResponse

def home(request):
    all = building.objects.all()
    context ={
        'all': all
    }
    return render(request, "tpu/home.html", context)

def building1(request):
    return render(request, 'tpu/building1.html' )

def building2(request):
    return render(request, 'tpu/building2.html' )

def building3(request):
    return render(request, 'tpu/building3.html' )
def map(request):
    return render(request, 'tpu/map.html')
