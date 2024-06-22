from django.urls import path
from myapp.views import index, about, contact, check_result

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('result/<str:task_id>', check_result, name='check_result')
]
