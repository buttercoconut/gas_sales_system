# README.md
# Gas Sales System

This project provides a backend API for managing gas sales contracts, customers, usage data, and payments, along with a simple Vue.js frontend that visualizes usage data.

## Backend
- FastAPI
- In-memory data store (for demo purposes)
- Endpoints:
  - `/contracts`
  - `/customers`
  - `/usage`
  - `/payments`

## Frontend
- Vue 3
- Chart.js for usage visualization

## Running
```bash
docker compose up --build
```

Backend will be available at `http://localhost:8000`.
Frontend will be available at `http://localhost:5173`.
