# Use an official Python runtime as a parent image
FROM python:3.10.13

# Working dir in docker
WORKDIR /app

# Copy the content to docker workdir
COPY . /app

# Install from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run uvicorn server when docker container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]