# Dockerfile
FROM python:3.12-slim

# Set env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Run Django
CMD ["gunicorn", "chainpesa.wsgi:application", "--bind", "0.0.0.0:8000"]
