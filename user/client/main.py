# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, redirect
import requests
import os, sys, time
import subprocess

time.sleep(2)
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

softversion = 1.2



# New updated stuff...


@app.route('/')
def home():
	return render_template('index.html', version=softversion)


@app.route('/settings')
def settings():
	return render_template('settings.html')


@app.route('/settings/sideload')
def sideloadhtml():
    return render_template('settings-sideload.html')

@app.route('/settings/api/sideload', methods=['GET','POST'])  
def sideload():
    if request.method == "POST":
        projectpath = request.form.get("textinput")
        output = subprocess.run(["python3", "test.py", projectpath], capture_output=True, text=True)
        output = output.stdout
        output = output.replace('\\n', '\n').replace('\\t', '\t')
        if output:
            return render_template('settings-sideload.html',output=output)
    return redirect('/settings/sideload')

@app.route('/settings/cupdate')
# Check for updates
def check_for_updates():
    url = "https://raw.githubusercontent.com/tuxisawesome/freeform/main/release/versions.txt"
    try:
        req = requests.get(url)
    except:
        print("Internal  - - Internet offline")
        return render_template('internet-err.html', version=softversion)
    if req.status_code in [200]:
        onlinev = req.text
    else:
        print("Internal  - - Internet offline")
        return render_template('internet-err.html', version=softversion)
        

    if softversion < float(onlinev):
        return render_template('cupdate-isupdate.html', cversion=softversion,uversion=onlinev)
    else:
        return render_template('cupdate-noupdate.html', version=softversion)

    


@app.route('/settings/update')
def update_system():
    url = "https://raw.githubusercontent.com/tuxisawesome/freeform/main/release/versions.txt"

    try:
        req = requests.get(url)
    except:
        print("Internal  - - Internet offline")
        return render_template('internet-err.html', version=softversion)

    if req.status_code in [200]:
        onlinev = float(req.text)
    else:
        print("Internal  - - Internet offline")
        return render_template('internet-err.html', version=softversion)

    if softversion < onlinev:
        # Begin update process
        os.system("python3 update.py &")
        return render_template('update.html')
    else:
        return render_template('cupdate-noupdate.html')

@app.route('/settings/error')
def error():
    # TODO: update system
	return render_template('error.html')

# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application
	# on the local development server.
	app.run(port=5002)
