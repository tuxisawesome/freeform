# Initialization procedure
from flask import Flask, render_template
import catalogLib, updateLib
import sys, requests

def create_default_catalogs():
    catalogLib.create_catalog("Userprefs", "User preferences", "userData/configurationData/0000-userData")
    catalogLib.create_catalog("Sysprefs", "System preferences", "userData/configurationData/0001-systemData")

userCatalog = catalogLib.read_catalog("userData/configurationData/0000-userData")
systemCatalog = catalogLib.read_catalog("userData/configurationData/0001-systemData")
app = Flask(__name__)

@app.route('/')
def home():
    # Pass dynamic data (optional) using keyword arguments
    user_name = catalogLib.get_entry(userCatalog, "username", 1)[1]
    return render_template('index.html', name=user_name)

@app.route('/settings/updatecheck')
def check_for_updates():
    current_version = float(catalogLib.get_entry(systemCatalog, "version", 1)[1])
    try:
        newversion = updateLib.get_latest_version_number()
    except:
        return "An unknown error occured"
    if current_version >= newversion: return render_template('system-softwareUpdate-updateCheck')
    else: return render_template('system-softwareUpdate-updateCheck-available', version=newversion)

if __name__ == '__main__':
    app.run(debug=False)