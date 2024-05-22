from celery import shared_task
from time import sleep

@shared_task
def tp1(queue='celery'):
	sleep(3)
	return


@shared_task
def tp2(queue='celery:1'):
	sleep(3)
	return


@shared_task
def tp3(queue='celery:2'):
	sleep(3)
	return


@shared_task
def tp4(queue='celery:3'):
	sleep(3)
	return

