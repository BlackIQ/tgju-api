# Use a minimal Python base image
FROM python:3.14-alpine

# UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --locked

# Copy the code into the container
COPY . .
