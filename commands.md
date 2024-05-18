### Make a "endpoint.sh" as executable.
chmod +x ./entrypoint.sh

### Build the docker compose file as a daemon. 
docker-compose up -d --build

### Open up a new terminal in Docker container.
Key "-t" is for virtual terminal.
Key "-i" is for using keyboard. 

docker exec -it django /bin/sh
