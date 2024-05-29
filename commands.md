### Make a "endpoint.sh" as executable.
    chmod +x ./entrypoint.sh

### Build the docker compose file as a daemon. 
    docker-compose up -d --build

### Open up a new terminal in Docker container.
    Key "-t" is for virtual terminal.
    Key "-i" is for using keyboard. 

    docker exec -it django /bin/sh

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


