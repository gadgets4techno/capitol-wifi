from flask import render_template, request, flash, Blueprint
#import platform
import mqtt as m, json
main = Blueprint('main', __name__)
#os=platform.get_platform()
m.init()

@main.route("/", methods=['GET'])
@main.route("/index", methods=['GET'])
def home():
 key = json.loads(str(m.payload))
 return render_template("main.html", networks=key["networks"], hidden_count=key["hidden"],deny_count=key["deny"],allow_count=key["allow"])

@main.route("/about")
def about():
 flash("If your SSID is on this site, you may be in trouble!!", "info")
 return render_template('about.html', title='About')

