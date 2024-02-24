from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
    # /pets routes
    from . import pets
    app.register_blueprint(pets.bp)
    # /facts routes
    from . import facts
    app.register_blueprint(facts.bp)

    return app
