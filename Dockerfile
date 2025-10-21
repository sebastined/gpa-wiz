# Dockerfile for gpa-wiz (Flask app)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install minimal system packages needed to build wheels + curl for healthcheck
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     build-essential gcc curl \
  && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt \
  && pip install --no-cache-dir gunicorn

# Copy app
COPY . /app

# Create non-root user and ensure permissions
RUN addgroup --system app \
 && adduser --system --ingroup app app \
 && chown -R app:app /app \
 && mkdir -p /app/reports && chown -R app:app /app/reports

# Use non-root user
USER app

# Expose the port your Flask app listens on (app.run uses 8080)
EXPOSE 8080

# Simple healthcheck using curl
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
  CMD curl -f http://127.0.0.1:8080/ || exit 1

# Run with Gunicorn; app.py must expose `app` (Flask instance)
CMD ["gunicorn", "--workers", "3", "--threads", "2", "--bind", "0.0.0.0:8080", "app:app"]
