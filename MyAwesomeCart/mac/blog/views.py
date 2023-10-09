from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    # if request.methods == "GET":
    return render(request, 'blog/index.html')
