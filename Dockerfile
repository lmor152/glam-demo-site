# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# download the goecoder data into the container
RUN python -c "from glam import Geocoder; Geocoder('glamdeps')"

# Copy the rest of the application code into the container
COPY . .

EXPOSE 8501



# Command to run the Streamlit app
CMD ["streamlit", "run", "app/home.py"]