# E-commerce Project

## Overview
This project is a simple e-commerce API built with Flask and PostgreSQL. It features a CI/CD pipeline using GitHub Actions and is deployed on Render.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`.
4. Set up a PostgreSQL database and update the `DATABASE_URL` in the `.env` file.
5. Run the application: `python app.py`.
6. Access Swagger UI at `http://localhost:5000/swagger/`.

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions, which automatically runs tests on every push to the `main` branch and deploys the app to Render if tests pass.

## Testing

To run tests, use the command: `python -m unittest discover -s tests`.

## Deployment

The application is deployed on Render. Use the provided Render link to access the live API.

