import os
import time

from celery import Celery
from kombu import Exchange, Queue
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery("cworker1")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True

# When the priority of tasks wasn't setted up manually, their priority will be 5.
app.conf.task_default_priority = 5

# "Prefetching" allows the worker to receive tasks before they will be processed.
# When "worker_prefetch_multiplier" equals "1" the worker will receive a new task only after handling the previous one.
# That allows us to avoid the situation when one or few tasks are stuck in the worker, who can't handle it at the time.
app.conf.worker_prefetch_multiplier = 1

# The "app.conf.worker_concurrency" parameter determines the number of threads, which the worker will use for the task compliting
app.conf.worker_concurrency = 1

@app.task(queue='tasks')
def t1():
    time.sleep(3)
    return

@app.task(queue='tasks')
def t2():
    time.sleep(3)
    return

@app.task(queue='tasks')
def t3():
    time.sleep(3)
    return

# app.conf.task_routes = {"cworker.tasks.*": {"queue": "queue1"},
#                         "cworker.tasks.task2": {"queue": "queue2"},
# 						}
# app.conf.task_default_rate_limit = "1/m"
# app.conf.broker_transport_options = {
# 	"priority_steps": list(range(10)),
# 	'sep': ":",
# 	"queue_ofrder_strategy": "priority"
# }
app.autodiscover_tasks()