from django.shortcuts import render
from celery.result import AsyncResult
from celeryproject.celery import add
from myapp.tasks import sub

# Create your views here.


# def index(request):
    # print('Index.......... ')
    # result1 = add.delay(20, 20)
    # print('result1>>>>>', result1)

    # result2 = sub.delay(80, 70)
    # print('result2>>>>>', result2)

    # return render(request, 'myapp/home.html')


# def index(request):
#     print('Index.......... ')
#     result1 = add.apply_async(args=[20, 30])
#     print('result1>>>>>', result1)

#     result2 = sub.apply_async(args=[100, 80])
#     print('result2>>>>>', result2)

#     return render(request, 'myapp/home.html')


# Display addition value after task execution
def index(request):
    result = add.delay(30, 30)
    return render(request, 'myapp/home.html', {'result':result})

def check_result(request, task_id):
    # Retrieve the task result usng task_id
    result = AsyncResult(task_id)
    print('Ready: ', result.ready())
    print('Successfull : ', result.successful())
    print('Ready: ', result.failed())
    
    # print('Get: ', result.get())

    return render(request, 'myapp/result.html', {'result':result})




def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

