from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('This is user index!')

def userLogin(request):
    return HttpResponse('This is user login!')