### Make a "endpoint.sh" as executable.
chmod +x ./entrypoint.sh

### Build the docker compose file as a daemon. 
docker-compose up -d --build

### Open up a new terminal in Docker container.
Key "-t" is for virtual terminal.
Key "-i" is for using keyboard. 

docker exec -it django /bin/sh

q### Executing a task
tp1.delay()

### Grouping a tasks
from celery import group

from cworker.tasks import tp1, tp2, tp3, tp4

tasks_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())

tasks_group.apply_async()

