# Use an official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock ./

# Install pipenv and project dependencies
RUN pip install pipenv \
    && pipenv install --system --deploy

# Copy the application code to the container
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "predict.py"]
