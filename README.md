# Simple Event-Driven Order System

This project was created to study **event-driven architecture** and working with **message brokers**.

The project does not have a traditional main branch. Instead, it uses two separate branches:

- `Kafka` — uses **Apache Kafka** as a message broker  
- `RabbitMQ` — uses **RabbitMQ** as a message broker

## Base Functions

- Create order  
- Get order by ID  
- Pay for order  
- Process order asynchronously  
- Cancel order  

## Project Structure

The project contains **4 services**, each of which can be built using its own `Dockerfile` and run independently:

- **Gateway service** — handles authentication and proxies requests to the Order service via gRPC  
- **Order service** — manages the database and acts as a producer for message brokers  
- **Payment and Fulfillment services** — mock services that consume messages from brokers  

## Simplifications

- **Authentication:** uses a static API key in the request header for simplicity  
- **Mock services:** payment and fulfillment services are simplified and do not implement real business logic; they only process event logs / queues  
- **Business logic:** intentionally simplified to focus on event-driven patterns  
- **Boilerplate:** some code is duplicated between services; it could be refactored into a separate shared package and used as a dependency

## Stack

- Python 3.12  
- FastAPI  
- Pydantic  
- gRPC  
- PostgreSQL  
- RabbitMQ / Apache Kafka  
- pytest  

## Launch

Run the project using Docker Compose:

```bash
docker compose up -d
```