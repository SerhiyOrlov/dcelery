### Make a "endpoint.sh" as executable.
    chmod +x ./entrypoint.sh

### Build the docker compose file as a daemon. 
    docker-compose up -d --build

### Open up a new terminal in Docker container.
    Key "-t" is for virtual terminal.
    Key "-i" is for using keyboard. 

    docker exec -it django /bin/sh

### Clean up docker
    key "-a" - Show all containers (default shows just running)
    key "-q" - Only display container IDs

    docker stop $(docker ps -aq) && docker rm $(docker ps -aq)  && docker rmi $(docker images -aq)


