from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
def bomra(request):
    return HttpResponse('<h1><marquee> BOOM BOOM BOOMRA</h1></marquee>')
