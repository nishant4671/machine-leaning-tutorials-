# Docker Syntax Cheatsheet 📝

| Command | Description | Example |
| :--- | :--- | :--- |
| `docker build -t name .` | Build an image from a Dockerfile | `docker build -t my-app .` |
| `docker run -p 80:80 img` | Run a container (map ports) | `docker run -p 8000:8000 my-app`|
| `docker ps` | List running containers | `docker ps` |
| `docker images` | List all local images | `docker images` |
| `docker stop [id]` | Stop a container | `docker stop a1b2` |
| `docker rm [id]` | Remove a container | `docker rm a1b2` |
| `docker rmi [img]` | Remove an image | `docker rmi my-app` |
| `docker exec -it [id] bash`| Open a terminal inside container | `docker exec -it a1b2 bash` |
| `docker pull [img]` | Download an image from Hub | `docker pull python:3.9` |
| `docker-compose up` | Run multi-container apps | `docker-compose up` |
