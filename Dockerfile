# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Set the Python path to include the /usr/src/app directory
# This ensures Python can find your local pixoo module
ENV PYTHONPATH=/usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run chess_stats.py when the container launches
CMD ["python", "./chess_stats.py"]
