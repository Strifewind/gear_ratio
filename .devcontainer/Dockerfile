FROM mcr.microsoft.com/devcontainers/python:3.11

# Install additional system packages
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create a non-root user (already done by devcontainer image, but ensuring permissions)
RUN groupadd -r appuser 2>/dev/null || true && \
    useradd -r -g appuser appuser 2>/dev/null || true

WORKDIR /workspace
