from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import LoginManager
from models import User

# Imported db reference from the db.py
from db import db

# Imported route_controller from routes.py
from routes import route_controller

# Import example data generator
from generate_data import generate_example_data

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# Temp profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

app.register_blueprint(route_controller)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db.init_app(app)

with app.app_context():
    db.create_all()

    # Generate Example Data if db empty.
    generate_example_data(db=db)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
