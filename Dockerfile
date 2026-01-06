# Use a minimal Python base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the CLI source code into the container
COPY . .

# Set the entrypoint to run the CLI
ENTRYPOINT ["python3", "wsgi.py"]