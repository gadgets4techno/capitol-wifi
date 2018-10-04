from flask import render_template, request, flash, Blueprint
#import platform
import mqtt as m, json
main = Blueprint('main', __name__)
m.init()

@main.route("/", methods=['GET'])
@main.route("/index", methods=['GET'])
def home():
 try:
  key = json.loads(str(m.payload))
  return render_template("main.html", networks=key["networks"], hidden_count=key["hidden"],deny_count=key["deny"],allow_count=key["allow"],media_count=key["media"],student_count=key["students"])
 except:
  flash("Reloading...", "warning")
  return render_template("main.html", networks="--", hidden_count="--",deny_count="--",allow_count="--",media_count="--", student_count="--")

@main.route("/about")
def about():
 flash("If your SSID is on this site, check your devices!", "info")
 return render_template('about.html', title='About')

