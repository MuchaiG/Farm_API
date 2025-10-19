# 🌱 Farm_API

Farm_API is a Django REST Framework–based backend for managing farm activities.  
It provides APIs for **user management, fields, crops, planting records, and production tracking**.

---

## 🚀 Features
- 👤 **User Authentication** (JWT-based: register, login, profile)
- 🌾 **Farm Management** (fields, crops, plantings)
- 📊 **Production Tracking** (production records, cost of production)
- 🔐 Role-based users (farmer, staff)

---

# API ENDPOINTS
- Farm_API uses JWT(JSON Web Tokens)
## Accounts
- Register -  **POST /api/accounts/register/**
    - Registers new user.

- Login -  **POST /api/accounts/login/**
    - This logs in user and returns *access* and *refresh* tokens to be used on requests: Authorization: Bearer <your_access_token>

- Profile - **GET /api/accounts/profile/**
    - This gets logged-in user details

- Token-Refresh - **POST /api/accounts/token/refresh/**
    - Gives you access to an updated authorization token.

## Farm
- Fields - **GET/POST /api/farm/fields/**
    - Lists or Creates farm fields.

- Crops - **GET/POST /api/farm/crops/**
    - Lists or Creates Crops in the farm.

- Plantings - **GET/POST /api/farm/platings/**
    - Lists or Creates crop planting records.

## Production
- Expenses - **GET/POST /api/production/expenses/**
    - Tracks cost of production.

# Example Test Cases
### 1. Register a User
    POST http://127.0.0.1:8000/api/accounts/register/
    Content-Type: application/json

    {
        "username": "farmer1",
        "email": "farmer1@example.com",
        "password": "testpass123",
        "role": "farmer",
        "phone": "+2547123456789"
    }

### 2. Login
    POST http://127.0.0.1:8000/api/accounts/login/
    Content-Type: application/json

    {
        "username": "farmer1",
        "password": "testpass123"
    }
**Response**

    {
        "refresh": "eyJhbGciOi...",
        "access": "eyJhbGciOi..."
    }

### 3. Create a Field

    POST http://127.0.0.1:8000/api/farm/fields/
    Content-Type: application/json
    Authorization: Bearer <access_token>

    {
        "name": "Green Farm",
        "owner": "Enter user id",
        "location": "Kagwe",
        "size_in_acres": 2.5
    }

### 4. Create a Crop

    POST http://127.0.0.1:8000/api/farm/crops/
    Content-Type: application/json
    Authorization: Bearer <access_token>

    {
        "name": "Zucchini",
        "crop_type": "VEG",
        "field": "Enter field id"
    }

### 5. Record Production

    POST http://127.0.0.1:8000/api/production/expenses/
    Content-Type: application/json
    Authorization: Bearer <access_token>

    {
        "planting": 1,
        "category": "seeds",
        "description": "example: 500g of Grade 1 seeds",
        "amount": 1500.00,
        "date_incurred": "2025-10-19"
        
    }

 





