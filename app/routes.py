from flask import redirect, render_template, request, url_for, flash, Blueprint
from app import db
from app.models import Cars, User, Order
from forms import CarForm, RegisterForm, LoginForm, OrderForm
from config import Config
import os
from flask_login import login_required, login_remembered, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

bp = Blueprint("main", __name__)
UPLOAD_FOLDER_CARS = Config.UPLOAD_FOLDER_CARS
UPLOAD_FOLDER_USERS = Config.UPLOAD_FOLDER_USERS

# ...............................................................................
@bp.context_processor
def inject_form():
    return dict(registerform=RegisterForm())

@bp.context_processor
def inject_form():
    return dict(loginform=LoginForm())

@bp.route('/')
def home():
    return render_template('home.html')

def add_user_orders(user_phone, user_id):
    orders = Order.query.filter_by(user_phone=user_phone).all()
    for order in orders:
        order.user_id = user_id  # Обновляем каждый заказ
    db.session.commit()


@bp.route('/register', methods=["GET", "POST"])
def register():
    registerform = RegisterForm()

    if registerform.validate_on_submit():
        hashed_password = generate_password_hash(registerform.user_password.data)
        
        new_user = User(
            user_name=registerform.user_name.data,
            user_password=hashed_password,
            user_phone=registerform.user_phone.data,
            user_email=registerform.user_email.data
        )
        
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash("Ви успішно зареєструвалися! Ви увійшли до аккаунту.", 'success')
        
        db.session.close()
        
        add_user_orders(new_user.user_phone, new_user.id)
        
        return redirect(url_for("main.home"))

@bp.route('/login', methods=["GET", "POST"])
def login():
    loginform = LoginForm()

    if loginform.validate_on_submit():
        user = User.query.filter_by(user_email=loginform.user_email.data).first()

        if user and check_password_hash(user.user_password, loginform.user_password.data):
            login_user(user)
            flash("Ви увійшли до аккаунту!", 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Неправильно написана пошта або пароль! Спробуйте ще раз.', 'danger')
            return redirect(url_for('main.home'))


@bp.route('/add_new_car', methods=["POST", "GET"])
def add_new_car():
    form = CarForm()
    
    if form.validate_on_submit():
        file = form.image.data
        if file:
            filestorage = os.path.join(UPLOAD_FOLDER_CARS, file.filename)
            with open(filestorage, 'wb') as f:
                f.write(file.read())
        
        new_car = Cars(car=form.car.data, brand=form.brand.data, price=form.price.data, body=form.body.data, image=file.filename)
        db.session.add(new_car)
        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template("add_new_car.html", form=form)


@bp.route('/cars', methods=["GET"])
def cars():
    cars = Cars.query.all()

    return render_template("cars.html", cars=cars)




@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Ви вийшли з профілю!", 'success')
    return redirect(url_for("main.home"))

@bp.route("/my_profile/<string:user_name>", methods=["GET", "POST"])
@login_required 
def my_profile(user_name):

    user = User.query.filter_by(user_name=user_name).first()
    if not user:
        flash('Користувача не знайдено!', 'warning')
        return redirect(url_for('main.home'))

    return render_template("my_profile.html", user=user)

@bp.route('/cars/create-order/<int:car_id>', methods=["GET", "POST"])
def create_order(car_id):
    form = OrderForm()
    car = Cars.query.filter_by(id=car_id).first()

    # Проверка существования автомобиля
    if car is None:
        flash("Машину не знайдено!", "error")
        return redirect(url_for('main.home'))
    
    if current_user.is_authenticated:
        del form.user_phone

    if form.validate_on_submit():
        total_price = float(form.total_price.data)

        if current_user.is_authenticated:
            user_id = current_user.id
            user_phone = current_user.user_phone
        else:
            user_id = None  # Указываем, что у незарегистрированного пользователя нет ID
            user_phone = form.user_phone.data # Используем номер телефона из формы
            

        # Преобразование даты в строку и времени в строку
        start_date_str = form.start_date.data.strftime('%Y-%m-%d')  # Дата в строку 'YYYY-MM-DD'
        start_time_str = form.start_time.data.strftime('%H:%M:%S')  # Время в строку 'HH:MM:SS'

        stop_date_str = form.stop_date.data.strftime('%Y-%m-%d')  # Дата в строку 'YYYY-MM-DD'
        stop_time_str = form.stop_time.data.strftime('%H:%M:%S')  # Время в строку 'HH:MM:SS'

        # Объединение даты и времени
        start_datetime_str = start_date_str + ' ' + start_time_str
        stop_datetime_str = stop_date_str + ' ' + stop_time_str

        # Преобразование строки в объект datetime
        start_date = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M:%S')
        stop_date = datetime.strptime(stop_datetime_str, '%Y-%m-%d %H:%M:%S')

        new_order = Order(
            car_id=car_id,
            start_date=start_date,
            stop_date=stop_date,
            total_price=total_price,
            user_id=user_id,
            user_phone=user_phone
        )

        
        
        db.session.add(new_order)
        db.session.commit()
        flash("Замовлення створено успішно!", "success")
        return redirect(url_for('main.home'))


    return render_template('create_order.html', form=form, car=car)

@bp.route('/edit')
def edit():

    cars = Cars.query.all()  # Получаем все машины из базы данных
    return render_template("edit.html", cars=cars)

@bp.route('/edit/del<int:car_id>')
def delete(car_id):
    car = Cars.query.filter_by(id=car_id).first_or_404()

    # Обрабатываем заказы, связанные с этим автомобилем
    orders = Order.query.filter_by(car_id=car_id).all()
    for order in orders:
        # Можно либо удалить заказы, либо обновить их, назначив другой car_id
        db.session.delete(order)  # Если нужно удалить заказы

    db.session.delete(car)
    db.session.commit()
    return redirect(url_for("main.edit"))
