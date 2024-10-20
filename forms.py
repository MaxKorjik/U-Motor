from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, HiddenField,  IntegerRangeField, StringField, PasswordField, SubmitField, FloatField, TextAreaField, IntegerField, DateField, TimeField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp
from flask_wtf.file import FileField, FileAllowed

class CarForm(FlaskForm):
    car = StringField("Машина", validators=[DataRequired()])
    brand = StringField("Марка авто", validators=[DataRequired()])
    price = FloatField("Ціна", validators=[DataRequired()])
    body = StringField("Кузов", validators=[DataRequired()])
    image = FileField('Фото авто', validators=[Optional(), FileAllowed(['jpg', 'png'], 'Тільки фото!')])
    submit = SubmitField("Надіслати")
    
class RegisterForm(FlaskForm):
    user_name = StringField("Ім'я", validators=[DataRequired()])
    user_password = PasswordField("Пароль", validators=[DataRequired()])
    user_email = EmailField("Пошта", validators=[DataRequired()])
    user_phone = StringField(
        "Номер телефону", 
        validators=[
            DataRequired(), 
            Regexp(
                r'^\d{3}-\d{3}-\d{2}-\d{2}$', 
                message="Номер телефону у форматі: XXX-XXX-XX-XX"
            )
        ]
    )
    submit = SubmitField("Зареєструватися")

class LoginForm(FlaskForm):
    user_email = EmailField("Пошта", validators=[DataRequired()])
    user_password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Увійти")
    
class OrderForm(FlaskForm):
    start_date = DateField('Дата початку оренди', format='%Y-%m-%d', validators=[DataRequired()])
    start_time = TimeField('Час початку оренди', validators=[DataRequired()])
    stop_date = DateField('Дата закінчення оренди', format='%Y-%m-%d', validators=[DataRequired()])
    stop_time = TimeField('Час закінчення оренди', validators=[DataRequired()])
    total_price = HiddenField('Всього до сплати')  # Скрытое поле для общей цены
    user_phone = StringField(
        "Номер телефону", 
        validators=[
            DataRequired(), 
            Regexp(
                r'^\d{3}-\d{3}-\d{2}-\d{2}$', 
                message="Номер телефону у форматі: XXX-XXX-XX-XX"
            )
        ]
    )

    submit = SubmitField('Створити замовлення')