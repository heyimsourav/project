from django.shortcuts import render
from django.http import HttpResponse
from .models import namedetail
# Create your views here.
def index(request):
    return render(request, 'index.html')

def entry(request):
    name1= namedetail()
    name1.std_name= request.POST['name']
    name1.std_roll= request.POST['Roll']
    name1.save()
    return render(request, 'index.html')

def show(request):
    post=namedetail.objects.all()
    return render( request, 'show.html', {'posts':post})