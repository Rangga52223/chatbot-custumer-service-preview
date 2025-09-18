# Base image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. Install dependency dasar
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# 3. Set workdir & copy project
WORKDIR /app
COPY . /app

# 4. Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# 5. Jalankan Ollama dan script Python
CMD ollama serve & sleep 5 && python3 run.py
