# 1. Use an official Python runtime as a parent image
FROM python:3.9-slim  

#this is the base image for our Docker container, which includes Python 3.9 and is a slim version to reduce the image size.

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy only the requirements first (for better caching)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# (For this tiny example, we'll just install one library)
RUN pip install --no-cache-dir fastapi uvicorn

# 4. Copy the rest of the application
COPY . .

# 5. Make port 8000 available to the world
EXPOSE 8000

# 6. Define the command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
