# Use the official Airflow image
FROM apache/airflow:latest

# Set working directory inside the container
WORKDIR /usr/local/airflow

# Copy the requirements.txt into the container
COPY ./train_service/requirements.txt /usr/local/airflow/requirements.txt

RUN python -m pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint for the container (this is usually not needed as it's part of the base image)
ENTRYPOINT ["bash", "-c", "airflow db init && airflow webserver"]