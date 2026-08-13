# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency definition and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files into container
COPY . .

# Expose port 7860
EXPOSE 7860

# Run Flask application using Gunicorn WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
