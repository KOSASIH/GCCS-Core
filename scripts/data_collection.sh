#!/bin/bash

# data_collection.sh

set -e  # Exit immediately if a command exits with a non-zero status

# Load configuration from YAML file
CONFIG_FILE="example_config.yaml"

# Function to collect sensor data
collect_sensor_data() {
    local device_id=$1
    local device_type=$2
    local location=$3

    if [ "$device_type" == "temperature" ]; then
        echo "{\"id\": \"$device_id\", \"type\": \"$device_type\", \"value\": $(awk -v min=-30 -v max=50 'BEGIN{srand(); print int(min+rand()*(max-min+1))}'), \"location\": \"$location\"}"
    elif [ "$device_type" == "humidity" ]; then
        echo "{\"id\": \"$device_id\", \"type\": \"$device_type\", \"value\": $(awk -v min=0 -v max=100 'BEGIN{srand(); print int(min+rand()*(max-min+1))}'), \"location\": \"$location\"}"
    fi
}

# Function to send data to the API
send_data_to_api() {
    local data=$1
    local api_endpoint="http://localhost:5000/api/climate"  # Update with actual API endpoint

    curl -X POST -H "Content-Type: application/json" -d "$data" "$api_endpoint"
}

# Main loop to collect and send data
while true; do
    # Example devices (you can modify this to read from the config file)
    devices=(
        "sensor_1 temperature Greenland"
        "sensor_2 humidity Amazon Rainforest"
    )

    for device in "${devices[@]}"; do
        IFS=' ' read -r id type location <<< "$device"
        sensor_data=$(collect_sensor_data "$id" "$type" "$location")
        send_data_to_api "$sensor_data"
        echo "Sent data: $sensor_data"
    done

    sleep 60  # Wait for 60 seconds before the next collection
done
