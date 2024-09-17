# Use Python 3.10 as the base image
FROM python:3.10-slim-buster

# Set the working directory (Set as root directory)
WORKDIR /app

# Copy requirements file and other necessary files (to root directory)
COPY requirements.txt ./
COPY .env ./
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "run.py"]