# from app import app, db
# from app.models import User
# from werkzeug.security import generate_password_hash, check_password_hash

# hashed_password = generate_password_hash('maximsuperadmin1234')


    
# with app.app_context():
#     admin = [User(user_name="Maxim", user_password=hashed_password, user_email='koshchinmaxim06@gmail.com', user_phone='0991006797', is_admin=True)]   
#     db.session.bulk_save_objects(admin)
#     db.session.commit()
    
# if __name__ == "__main__":
#     app.run(debug=True)