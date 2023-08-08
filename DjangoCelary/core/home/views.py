from django.shortcuts import render, redirect
from django.http import HttpResponse
import time
from home.task import *

def home(request):
    handle_sleep.delay()
    return HttpResponse('Hello from celery')