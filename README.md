markdown

# Khalifa E-Commerce System

This project is an e-commerce system that provides various API endpoints for managing authentication, user information, and product categories. The system runs using Docker to ensure consistent and easy deployment.

## Features

- User authentication and authorization
- CRUD operations for user information
- Product category management

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>

Environment Variables

Ensure you have all the necessary environment variables set in your .env file for the production environment.
Build and Run the Application

To build and run the application using Docker Compose, use the following command:

bash

sudo docker compose -f docker-compose.prod.yaml up -d --build

This command will build the Docker images and start the containers in detached mode.
API Documentation

The API documentation is generated using OpenAPI and can be accessed once the server is running.
Accessing the Documentation

After the server is up, you can access the documentation by navigating to /redoc or /docs on your server's domain.

For example:

arduino

http://yourdomain.com/redoc

API Endpoints
Authentication

    POST /auth/confirm-code
        Request Body:

        json

{
  "email": "user@example.com",
  "confirm_code": 0
}

Response:

json

        {
          "email": "user@example.com",
          "confirm_code": 0
        }

    POST /auth/create

    POST /auth/logout

    POST /auth/token

    GET /auth/user-info

    GET /auth/user-list

    PUT /auth/user-update

Category Management

    GET /api/category-list
        Query Parameters:
            name: string (optional)
            ordering: string (optional)
            search: string (optional)
            page: integer (optional)
        Response:

        json

        {
          "count": 0,
          "next": "http://example.com",
          "previous": "http://example.com",
          "results": [
            {
              // category details
            }
          ]
        }

Stopping the Application

To stop the running application, use the following command:

bash

sudo docker compose -f docker-compose.prod.yaml down
