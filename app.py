from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from swagger import configure_swagger

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
ma = Marshmallow(app)


from routes import api
app.register_blueprint(api)

# Configure Swagger
configure_swagger(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run()
