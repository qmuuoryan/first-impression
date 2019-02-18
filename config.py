import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:1234@localhost/pitch'
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD  = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:1234@localhost/pitch'
    DEBUG = True


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ryan:1234@localhost/pitch_test'


config_options = {
    "test": TestConfig,
    "production": ProdConfig,
    "development": DevConfig
}