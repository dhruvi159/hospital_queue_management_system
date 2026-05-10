# Hospital Management System

A scalable microservices-based Hospital Management System designed to streamline appointment booking, patient queue management, audit logging, and inter-service communication using modern distributed system technologies.

---

# Table of Contents
- Overview
- Features
- System Architecture
- Tech Stack
- Project Structure
- Installation & Setup
- Docker Deployment
- API Endpoints
- gRPC Integration
- Message Queue System
- Database Design
- Fault Tolerance
- Screenshots
- Future Improvements
- Learning Outcomes
- Contributors
- License

---

# Overview
The Hospital Management System is a distributed healthcare application developed using Python Flask, PostgreSQL, MongoDB, gRPC, ActiveMQ, and Docker. The project demonstrates real-world implementation of microservices architecture, asynchronous communication, audit logging, and scalable deployment.

The system allows patients to book appointments online while enabling administrators to manage hospital queues and appointment records efficiently.

---

# Features

## Patient Features
- Online appointment booking
- Real-time queue management
- Appointment tracking
- User-friendly interface

## Admin Features
- Manage patient appointments
- Monitor appointment queues
- Access audit logs
- View system activity

## Technical Features
- REST API integration
- gRPC communication
- ActiveMQ asynchronous messaging
- PostgreSQL database integration
- MongoDB audit logging
- Docker containerization
- Circuit Breaker fault tolerance
- Distributed microservices architecture

---

# System Architecture

The application follows a microservices architecture where multiple services communicate using REST APIs, gRPC, and messaging queues.

## Components

### Frontend Service
Handles user interactions for appointment booking and queue viewing.

### Backend Service
Processes appointment requests, queue operations, API handling, and database communication.

### PostgreSQL Database
Stores structured hospital and appointment-related data.

### MongoDB Service
Maintains audit logs and activity tracking.

### gRPC Service
Provides efficient high-speed communication between internal services.

### ActiveMQ Message Broker
Handles asynchronous communication and event-based notifications.

### Docker Environment
Containerizes all services for easier deployment and scalability.

---

# Tech Stack

## Backend
- Python
- Flask
- gRPC
- Protocol Buffers

## Databases
- PostgreSQL
- MongoDB

## Messaging & Communication
- ActiveMQ
- STOMP Protocol

## Deployment
- Docker
- Docker Compose

## Frontend
- HTML
- CSS
- JavaScript

---

# Project Structure

```bash
hospital-management-system/
│
├── frontend/                 # Frontend application
├── backend/                  # Flask backend services
├── grpc/                     # gRPC services and protobuf files
├── database/                 # Database configuration
├── audit-service/            # MongoDB audit logging
├── activemq/                 # Messaging queue configuration
├── docker-compose.yml        # Docker orchestration
├── requirements.txt          # Python dependencies
└── README.md
```

---

# Installation & Setup

## Prerequisites
Make sure the following are installed:

- Python 3.x
- Docker
- Docker Compose
- PostgreSQL
- MongoDB
- ActiveMQ

---

## Clone Repository

```bash
git clone <repository-url>
cd hospital-management-system
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Docker Deployment

## Build and Start Containers

```bash
docker-compose up --build
```

## Stop Containers

```bash
docker-compose down
```

Docker Compose automatically starts:
- Backend services
- PostgreSQL
- MongoDB
- ActiveMQ
- Supporting microservices

---

# API Endpoints

## Appointment APIs

### Book Appointment
```http
POST /appointments
```

### Get Queue Details
```http
GET /queue
```

### Get Appointment Details
```http
GET /appointments/<id>
```

### Delete Appointment
```http
DELETE /appointments/<id>
```

---

# gRPC Integration

The project uses gRPC for efficient inter-service communication.

## Features of gRPC Used
- Faster communication
- Protocol Buffers serialization
- Lightweight data transfer
- Internal service communication

## Example Use Cases
- Queue synchronization
- Service-to-service communication
- Real-time updates

---

# Message Queue System

ActiveMQ is used for asynchronous communication.

## Workflow
1. User books appointment.
2. Backend publishes event to queue.
3. Other services consume messages independently.
4. Audit service logs activity.

This improves:
- Scalability
- Reliability
- Loose coupling between services

---

# Database Design

## PostgreSQL Tables
- Patients
- Appointments
- Queue Information
- Hospital Records

## MongoDB Collections
- Audit Logs
- User Activity Logs
- System Events

---

# Fault Tolerance

The application uses the Circuit Breaker pattern using PyBreaker.

## Benefits
- Prevents cascading failures
- Handles temporary service outages
- Improves system stability
- Enables automatic recovery

If a dependent service fails repeatedly:
- Requests are temporarily blocked.
- The system waits before retrying.
- Recovery occurs automatically after timeout.

---

# Screenshots

Add screenshots of:
- Homepage
- Appointment Booking Page
- Queue Dashboard
- Admin Panel
- Docker Containers Running
- API Testing

---

# Future Improvements

- Authentication and Authorization
- Doctor management module
- Payment gateway integration
- AI-based appointment scheduling
- SMS/Email notifications
- Cloud deployment using AWS or Azure
- Kubernetes orchestration
- Mobile application support

---

# Learning Outcomes

This project helped in understanding:

- Microservices architecture
- Distributed systems
- REST API development
- gRPC communication
- Message queues and asynchronous systems
- Database management
- Docker containerization
- Fault-tolerant architectures
- Real-world backend system design

---

# Contributors

- Dhruvi Lolariya
- Devanshi Sanghvi

---

# Conclusion

The Hospital Management System demonstrates how modern distributed technologies can work together to build scalable, reliable, and maintainable healthcare applications. The project combines REST APIs, gRPC communication, asynchronous messaging, databases, and Docker deployment to simulate an enterprise-level hospital management workflow.

The Hospital Management System demonstrates how modern distributed technologies can work together to build scalable, reliable, and maintainable healthcare applications. The project combines REST APIs, gRPC communication, asynchronous messaging, databases, and Docker deployment to simulate an enterprise-level hospital management workflow.
