from django.shortcuts import render
from django.http import HttpResponse
from .models import Accounts


def index(request):
    return HttpResponse('Home Accounts')
