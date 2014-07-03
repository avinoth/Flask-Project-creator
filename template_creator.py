import os
import urllib
import urllib2


project = raw_input("Enter the Project name")
app_path = os.path.dirname(os.path.abspath(__file__)) + "\%s" % (project,)
pkg_path = app_path + "\%s" % (project,)
static = pkg_path + "\static"
if not os.path.exists(app_path):
    os.makedirs(app_path)
    os.makedirs(pkg_path)
    os.makedirs(static)
    os.makedirs(pkg_path + "\\templates")

with open(app_path + "\\runserver.py", 'w') as rserver:
    rserver.write(
"""from %s import app
app.run(debug=True)""" % (project,))

with open(pkg_path + "\\__init__.py", 'w') as init:
    init.write(
"""from flask import Flask
app = Flask(__name__)
import %s.views""" % (project))
    
with open(pkg_path + "\\views.py", 'w') as views:
    views.write(
"""from %s import app
@app.route('/')
def index():
    return 'Hello World!'""" % (project))



print "Project Structure successfully created"
