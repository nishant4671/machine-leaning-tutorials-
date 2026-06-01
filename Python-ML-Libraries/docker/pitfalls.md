# Docker Pitfalls ⚠️

1. **Large Images**: Using `FROM python:3.9` instead of `python:3.9-slim`. It can make your image 1GB bigger for no reason!
   *Fix*: Use `-slim` or `-alpine` base images.

2. **Forgotten `requirements.txt`**: Your code crashes because a library is missing.
   *Fix*: Always `COPY requirements.txt` and `RUN pip install` before copying the rest of your code.

3. **Wrong CMD**: The container starts and immediately stops.
   *Fix*: Ensure your `CMD` points to a long-running process (like a web server).

4. **Caching Issues**: Not understanding that Docker caches each line (layer) of your Dockerfile.
   *Fix*: Put instructions that change often (like `COPY . .`) at the bottom.

5. **Exposing Wrong Ports**: Your app is running on 8080, but you mapped 8000.
   *Fix*: Double check your `EXPOSE` and `docker run -p` commands.
