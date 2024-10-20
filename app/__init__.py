from app.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

db.init_app(app)
csrf.init_app(app) 
login_manager.init_app(app)
login_manager.login_view = 'main.login'

from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
migrate = Migrate(app, db)

from app import routes
app.register_blueprint(routes.bp)



