# Docker Commands

To build image from `Dockerfile`

`docker build -f Dockerfile rsharma96/py-agentai-testapp:latest`

To push built docker image to docker hub

`docker push rsharma96/py-agentai-testapp:latest`

To run docker image as a container

`docker run -it rsharma96/py-agentai-testapp:latest`

To run docker image as a container with port expose

`docker run -it -p 3000:8000 rsharma96/py-agentai-testapp:latest`

`3000`: on local system `8000`: inside container

To build image from `docker-compose.yaml`

`docker compose up` or `docker compose up --remove-orphans`

To build image using **docker-compose**

```yaml
services:
    app:
        build:
            context: .
            dockerfile: Dockerfile
    ports:
        - 3000:8000
    command: python -m http.server 8000
```

`docker compose build` and then to run `docker compose up`

To build and run using single command

`docker compose up` or `docker compose up --build`

