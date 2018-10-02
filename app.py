from cloudant import Cloudant
from flask import Flask, render_template, request, url_for, flash, Blueprint
import os, atexit, json
app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))


if __name__ == "__main__":
   app.config['SECRET_KEY'] = 'T#CHN02H3H#50'
   app.config['SESSION_TYPE'] = 'filesystem'
   from errors.handlers import errors
   from main.routes import main
   app.register_blueprint(errors)
   app.register_blueprint(main)
   app.run(host='0.0.0.0', port=port, debug=True)
