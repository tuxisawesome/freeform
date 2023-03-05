# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

softversion = "1.0.0"

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
