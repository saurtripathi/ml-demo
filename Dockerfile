# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory
# WORKDIR /app
WORKDIR /ml-demo


# Copy all files
# COPY . /app
COPY . /ml-demo

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
