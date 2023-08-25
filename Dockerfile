# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Python to ensure it doesn't try to buffer outputs and to use UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Update the repository and install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment varibles for debugging purposes
ENV DJANGO_DEBUG=True

# Set the working directory in docker
WORKDIR /app

# Copy the current directory contents into the container at /app/
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose port 8003
EXPOSE 8003

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]