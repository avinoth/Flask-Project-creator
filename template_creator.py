import os
import urllib
import urllib2


project = raw_input("Enter the Project name")
app_path = os.path.dirname(os.path.abspath(__file__)) + "\%s" % (project,)
pkg_path = app_path + "\%s" % (project,)
static = pkg_path + "\static"
templates = pkg_path + "\templates"
if not os.path.exists(app_path):
    os.makedirs(app_path)
    os.makedirs(pkg_path)
    os.makedirs(static)
    os.makedirs(templates)

#Create Runserver.py file
with open(app_path + "\\runserver.py", 'w') as rserver:
    rserver.write(
"""from %s import app
app.run(debug=True)""" % (project,))

#Create __init__.py file inside the application package
with open(pkg_path + "\\__init__.py", 'w') as init:
    init.write(
"""from flask import Flask
app = Flask(__name__)
import %s.views""" % (project))

#Create views.py as a placeholder py file 
with open(pkg_path + "\\views.py", 'w') as views:
    views.write(
"""from %s import app
@app.route('/')
def index():
    return 'Hello World!'""" % (project))

#creating template files
with open(templates + "\\layout.html") as lout:
          lout.write(
"""
<!DOCTYPE html>
<html>
<head>
Enter heading here
</head>
<body>
<p> Some body content here...</p>
</body>
</html>""")

with open(templates + "\\home.html") as home:
          home.write(
"""
<!DOCTYPE html>
<html>
<head>
Enter heading here
</head>
<body>
<p> Some body content here...</p>
</body>
</html>""")    



print "All Done"
