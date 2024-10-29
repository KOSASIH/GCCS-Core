# API Documentation

## Overview
The GCCS-Core API provides a set of endpoints for accessing climate data and managing geoengineering interventions. The API follows RESTful principles and returns data in JSON format.

## Base URL

[http://localhost:5000/api](http://localhost:5000/api) 


## Endpoints

### 1. Get Current Climate Data
- **Endpoint**: `/climate`
- **Method**: `GET`
- **Description**: Retrieves the latest climate data from the system.
- **Response**:
  ```json
  1 {
  2   "temperature": 22.5,
  3   "humidity": 60,
  4   "co2_level": 400
  5 }
  ```

  ### 2. Submit Geoengineering Intervention
- **Endpoint**: /interventions
- **Method**: POST
- **Description**: Submits a request for a geoengineering intervention.
- **Request Body**:
  ```json
  1 {
  2   "type": "carbon_capture",
  3   "parameters": {
  4   "location": "North America",
  5   "duration": "6 months"
  6  }
  7 }
  ```
  
- Response:

  ```json
  1 {
  2   "status": "success",
  3   "message": "Intervention submitted successfully."
  4 }
  ```

## Error Handling
The API returns standard HTTP status codes to indicate the success or failure of requests. Common error responses include:

- 400 Bad Request: Invalid input data.
- 404 Not Found: Endpoint not found.
- 500 Internal Server Error: An unexpected error occurred.

# Conclusion
This API documentation provides a comprehensive overview of the available endpoints and their usage. For further assistance, please refer to the user guide or contact support.
