# Use official Python image as base
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy requirements file first (for caching)
COPY xyz.py .

# Copy all project files into container
COPY . .

# Expose port (change if your app uses different port)
EXPOSE 5000

# Command to run the application
CMD ["python", "xyz.py"]