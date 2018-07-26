from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'website/index.html', {})

def ideals(request):
    return render(request, 'website/ideals.html', {})

def members(request):
    return render(request, 'website/members.html', {})

def projects(request):
    return render(request, 'website/projects.html', {})

def presentations(request):
    return render(request, 'website/presentations.html', {})
# Create your views here.
