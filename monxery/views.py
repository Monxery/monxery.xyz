from django.shortcuts import render
from .models import *

def index(request):
    news = News.objects.all()
    context = {'news':news}
    return render(request, 'index.html', context)
# Create your views here.
