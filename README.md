# Healthcare-WhatBytes

An API developed for the WhatBytes internship assignment.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This project is a backend system for a healthcare application. It provides functionalities to manage patient and doctor records securely, handle user authentication, and facilitate the mapping between patients and doctors.

## Features

- **User Authentication**: Secure user registration and login.
- **Patient Management**: CRUD operations for patient records.
- **Doctor Management**: CRUD operations for doctor records.
- **Patient-Doctor Mapping**: Assign doctors to patients and manage these mappings.
- **Security**: Endpoints are secured with proper permissions.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Environment Management**: Python-dotenv

## Setup and Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Sufail07/Healthcare-WhatBytes.git
    cd Healthcare-WhatBytes
    ```

2. **Create a Virtual Environment and Activate It**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:

    Create a `.env` file in the project root and add the following configurations:

    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_NAME=your_db_name
    DATABASE_USER=your_db_user
    DATABASE_PASSWORD=your_db_password
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```

5. **Apply Migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a Superuser (Optional)**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the Development Server**:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

The API provides the following endpoints:

- **Authentication**:
  - `POST /api/auth/register/`: Register a new user.
  - `POST /api/auth/login/`: Log in a user and receive JWT tokens.

- **Patient Management**:
  - `POST /api/patients/`: Create a new patient.
  - `GET /api/patients/`: Retrieve all patients.
  - `GET /api/patients/{id}/`: Get details of a specific patient.
  - `PUT /api/patients/{id}/`: Update patient details.
  - `DELETE /api/patients/{id}/`: Delete a patient record.

- **Doctor Management**:
  - `POST /api/doctors/`: Create a new doctor.
  - `GET /api/doctors/`: Retrieve all doctors.
  - `GET /api/doctors/{id}/`: Get details of a specific doctor.
  - `PUT /api/doctors/{id}/`: Update doctor details.
  - `DELETE /api/doctors/{id}/`: Delete a doctor record.

- **Patient-Doctor Mapping**:
  - `POST /api/mappings/`: Assign a doctor to a patient.
  - `GET /api/mappings/`: Retrieve all mappings.
  - `GET /api/mappings/{patient_id}/`: Get doctors assigned to a specific patient.
  - `DELETE /api/mappings/{id}/`: Remove a doctor from a patient.

