from django.shortcuts import render
from django.http import HttpResponse
import utils

# Create your views here.

def index(request):

    ip = request.GET['ip']
    country = utils.tonation(ip)
    return HttpResponse(country)
