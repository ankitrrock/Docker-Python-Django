# Use an official Python runtime as a base image
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app/docker_python_django

# Copy the current directory contents into the container at /app
COPY . /app/docker_python_django

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 to allow communication to/from server
EXPOSE 8000

# Command to run the Django application
CMD ["python", "docker_python_django/manage.py", "runserver", "0.0.0.0:8000"]




