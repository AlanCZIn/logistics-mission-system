# Logistics Mission System

Backend system for managing logistics missions with:

- Role-based access (ADMIN / OPERATOR)
- Mission state machine
- Operator capacity control
- Mission reassignment
- Audit history tracking
- Dockerized environment
- PostgreSQL database

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- JWT Authentication (in progress)

## Project Structure

app/
- core/ → configuration & database
- models/ → database models
- services/ → business logic
- repositories/ → data access layer
- api/ → routes
- schemas/ → Pydantic schemas

## How to Run

```bash
docker compose up --build

