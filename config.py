import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLAlchemy settings
    # For now using SQLite for easy setup, but ready for MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
