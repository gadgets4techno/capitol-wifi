from flask import Flask

def create_app():
 app = Flask(__name__)
 app.config['SECRET_KEY'] = 'T#CHN02H3H#50'
 from app.errors.handlers import errors
 from app.main.routes import main

 app.register_blueprint(errors)
 app.register_blueprint(main)
 return app

