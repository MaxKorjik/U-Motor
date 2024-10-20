import os 

class Config:
    SECRET_KEY = "kihLhvpg9KJvUYjhvbp9i234BHGg24vLjvu8i2fgpoGJHFDjiyduty7UGGOHl35gbuihb7JKIhgbf23ojv29oi9JHNh3hdhneuohgw2t4t"
    SQLALCHEMY_DATABASE_URI = "sqlite:///u_motor.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True

    UPLOAD_FOLDER_CARS = "./app/static/photos/cars"
    UPLOAD_FOLDER_USERS = "./app/static/photos/users"