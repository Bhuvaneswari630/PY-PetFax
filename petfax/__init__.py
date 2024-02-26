from flask import Flask 
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    # /pets routes
    from . import pets
    app.register_blueprint(pets.bp)
    # /facts routes
    from . import facts
    app.register_blueprint(facts.bp)

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    return app


            

