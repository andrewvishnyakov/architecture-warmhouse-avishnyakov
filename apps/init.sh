#!/bin/bash

# Exit on any error
set -e

echo "Starting the Smart Home Sensor API..."
echo "Building and starting containers..."
sudo docker-compose up --build -d

echo "Waiting for services to be ready..."


echo "All services are up and running!"
echo "The API is available at http://localhost:8081"
echo ""
echo "To view logs, run: docker-compose logs -f"
echo "To stop the services, run: docker-compose down"