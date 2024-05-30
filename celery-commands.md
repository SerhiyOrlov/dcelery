### Executing a task
    tp1.delay()


from cworker.tasks import tp1, tp2, tp3, tp4
### Grouping a tasks
    from celery import group
    tasks_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s()) -- Set the group.
    tasks_group.apply_async() -- Run the group.

### Chaining a tasks
    from celery import chain
    task_chain = chain(tp1.s(), tp2.s(), tp3.s()) -- Set the chain.
    task_chain.apply_async() -- Run the chain.

### Task rate limit setting
    app.conf.task_default_rate_limit = "1/m" -- Execute one task in 1 minute

### Set the default task priority
    When the priority of tasks wasn't setted up manually, their priority will be 5.

    app.conf.task_default_priority = 5

### Set the prefetching multiplier
    "Prefetching" allows the worker to receive tasks before they will be processed.
    When "worker_prefetch_multiplier" equals "1" the worker will receive a new task only after handling the previous one.
    That allows us to avoid the situation when one or few tasks are stuck in the worker, who can't handle it at the time.

    app.conf.worker_prefetch_multiplier = 1

### Set the worker concurrency
    The "app.conf.worker_concurrency" parameter determines the number of threads, which the worker will use for the task compliting.
    app.conf.worker_concurrency = 1 

### Prioritization of the tasks
    from config.celery import *
    t2.apply_async(priority=5)
    t1.apply_async(priority=6)
    t3.apply_async(priority=9)
    t1.apply_async(priority=6)
    t2.apply_async(priority=5)
    t3.apply_async(priority=9)

### Ispect task(Run on Django)
    celery inspect active
    celery inspect active_queues

### Provide the positional and keywoards arguments to the task
    Task example:
    -----------------------------------
    @app.task()
    def t1(a, b, message=None):
        result = a + b
        if message:
            result = f"{message}: {result}"
        return result
    ------------------------------------
    Execution of the task:
    ------------------------------------

    t1.apply_async(args=[5,10], kwargs={"message": "The sum is"})

    ------------------------------------
    Actions with the task object:
    ------------------------------------
    task_object = t1.apply_async(args=[5,10], kwargs={"message": "The sum is"}) - Save task object to the variable.
        task_object.ready() - Checks whether the task is completed or not.
        task_object.successful() - Checks whether the task was completed without errors.
        task_object.get() - Get the result of the task.
        task_object.getResult() = Returns if the task has completed successfully.
        task_object.get(propagate=False) = Returns if the exception or error.
