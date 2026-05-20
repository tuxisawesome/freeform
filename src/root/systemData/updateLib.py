import requests

baseURL = "https://github.com/tuxisawesome/freeform/raw/refs/heads/main/sysupdate"
def get_latest_version_number():
    newv = float(requests.get(f"{baseURL}/newversion.txt").text)
    print(f"Checked for update, current version is {newv}")
    return newv