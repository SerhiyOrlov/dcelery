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

app.conf.task_default_priority = 5

app.conf.worker_prefetch_multiplier = 1

app.conf.worker_concurrency = 1

@app.task(queue='tasks')
def t1(a, b, message=None):
    result = a + b
    if message:
        result = f"{message}: {result}"
    return result

def test():
    result = t1.apply_async(args=[5,10], kwargs={"message":"The sum is"})

    # Check is the task has completed
    if result.ready():
        print("Task has completed")
    else:
        print("Task is still running")

    #Check if the task completed successfully
    if result.successful():
        print("Task completed successfully")
    else:
        print("Task encountered an error")

    # Fet the result of the task
    try:
        task_result = result.get()
        print(f"Task result: {task_result}")
    except Exception as e:
        print(f"An exception occured: {e}")

    # Get the exception (if any) that occurred during task execution
    exception = result.get(propagate=False)
    if exception:
        print(f"An exception occurred during task execution {exception}")

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