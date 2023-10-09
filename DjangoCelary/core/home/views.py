from django.shortcuts import render, redirect
from django.http import HttpResponse
import time
from home.task import handle_sleep

def home(request):
    handle_sleep.delay()
    return HttpResponse('Hello from celery')