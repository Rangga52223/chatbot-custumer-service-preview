# Gunakan base image Ubuntu
FROM ubuntu:22.04

# Set environment agar tidak interaktif
ENV DEBIAN_FRONTEND=noninteractive

# --- 1. Install dependency dasar ---
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# --- 2. Install Ollama ---
RUN curl -fsSL https://ollama.com/install.sh | sh

# --- 3. Download model llama3.2:3b ---
RUN ollama pull llama3.2:3b

# --- 4. Copy project ke dalam container ---
WORKDIR /app
COPY . /app

# --- 5. Install Python dependencies ---
RUN pip3 install --no-cache-dir -r requirements.txt

# --- 6. Jalankan Python script ---
CMD ["python3", "run.py"]
