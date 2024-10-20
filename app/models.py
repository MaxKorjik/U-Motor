from app import db
from flask_login import UserMixin
from datetime import datetime

# Модель автомобилей
class Cars(db.Model):
    __tablename__ = 'cars'  # Явно указываем имя таблицы
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)  # Цена за день
    body = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False, default="default.png")
    
    # Убедитесь, что backref уникален
    orders = db.relationship('Order', back_populates='car', lazy=True)

# Модель пользователей
class User(UserMixin, db.Model):
    __tablename__ = 'user'  # Явно указываем имя таблицы
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(110),  nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_phone = db.Column(db.String, unique=True, nullable=False)
    user_photo = db.Column(db.String, nullable=False, default="default.png")
    is_admin = db.Column(db.Boolean, default=False)

    # Убедитесь, что backref уникален
    orders = db.relationship('Order', backref='user_relationship', lazy=True)

# Модель заказов
class Order(db.Model):
    __tablename__ = 'order'  # Явно указываем имя таблицы
    id = db.Column(db.Integer, primary_key=True)
    
    # Связь с зарегистрированным пользователем (может быть пустым)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    # Номер телефона для незарегистрированного пользователя (может быть пустым)
    user_phone = db.Column(db.String, nullable=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    stop_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    car = db.relationship('Cars', back_populates='orders')
