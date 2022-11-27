from flask import Flask
from config.database import db
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
from routes.routes import blue_print
from flask_cors import CORS
import datetime
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

# Load the configuration from the instance Data Base
db_usuario = os.getenv('USER_DB')
db_clave = os.getenv('PASS_DB')
db_host = os.getenv('HOST_DB')
db_name = os.getenv('NAME_DB')
db_port = os.getenv('PORT_DB')

DB_URL = f'mysql+pymysql://{db_usuario}:{db_clave}@{db_host}:{db_port}/{db_name}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

# Initialization SQLAlchemy
db.init_app(app)

# instance routes
app.register_blueprint(blue_print)

# Create the database
with app.app_context():
    if not database_exists(DB_URL):
        create_database(DB_URL)
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
