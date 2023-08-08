from celery import shared_task
import time

@shared_task
def handle_sleep():
    print('handle sleep started')
    time.sleep(10)