# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
import requests

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


url = "https://raw.githubusercontent.com/tuxisawesome/freeform/main/release/versions.txt"

req = requests.get(url)
if req.status_code in [200]:
    softversion = req.text
else:
    print('Could not retrieve: %s, err: %s - status code: %s' % (url, req.text, req.status_code))
    softversion = "< Error retreving version >"
print(softversion)
@app.route('/')
def home():
	return render_template('index.html')


@app.route('/settings')
def settings():
	return render_template('settings.html')


@app.route('/settings/cupdate')
# Check for updates
def check_for_updates():
    # TODO: check for update code
	return render_template('cupdate-noupdate.html', version=softversion)


@app.route('/settings/update')
def update_system():
    # TODO: update system
	return render_template('update.html')

# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
