import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:newyork12@localhost:5432/ecommerce_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

