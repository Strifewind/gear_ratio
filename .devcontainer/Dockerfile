# syntax=docker/dockerfile:1.4
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user (optional)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Enable SSH forwarding for BuildKit
# Example: RUN --mount=type=ssh git clone git@github.com:your/private-repo.git

# Set work directory
WORKDIR /workspace

# Upgrade pip and install requirements if present
COPY requirements.txt* /workspace/
RUN pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Switch to non-root user
USER $USERNAME