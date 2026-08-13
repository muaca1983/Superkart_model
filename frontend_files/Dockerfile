# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency definition and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend application files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
