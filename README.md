# N-Queens Puzzle

This service solves the N-Queens Puzzle.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [How It Works](#how-it-works)
- [Running the Service](#running-the-service)
- [API Endpoints](#api-endpoints)

## Getting Started

This service is built using Python and FastAPI to solve the N-Queens puzzle efficiently. It checks the PostgreSQL database for existing solutions before performing calculations, ensuring optimal performance.

### Prerequisites

- [Docker](https://www.docker.com/get-started) (for running the service)
- [Docker Compose](https://docs.docker.com/compose/) (for managing multi-container applications)

## How It Works

To get started, you need to build and run the service using Docker Compose. 

### Running the Service

1. **Build the Docker image**:

    ```bash
    docker-compose build
    ```

2. **Start the service**:

    ```bash
    docker-compose up
    ```

### API Endpoints

The service exposes the following API endpoints:

- **Get All Stored Solutions**:
  - **Endpoint**: `GET localhost:8000/`
  - **Description**: Retrieves all stored N-Queens solutions from the database.

- **Get Solution for a Specific Board Size**:
  - **Endpoint**: `GET localhost:8000/puzzle`
  - **Query Parameter**: `n` (the board size)
  - **Example**: `localhost:8000/puzzle?n=5`
  - **Description**: Returns the solution for the specified N-Queens board size. If the solution has been calculated before, it will fetch it from the database.
