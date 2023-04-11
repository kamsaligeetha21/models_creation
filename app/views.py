from django.shortcuts import render
from app.models import *
# Create your views here.

def Topic(request):
    return render(request,'Topic',d)
