import os
import requests

baseURL = "https://github.com/tuxisawesome/freeform/raw/refs/heads/main/sysupdate"

url = f'{baseURL}/updateFile.zip'



def main():
    # Recieved update trigger
    import time
    print("Stage 1 == Sleeping 5 seconds to allow client to display page...")
    time.sleep(5)
    print("Stage 2 == Download file")
    with requests.get(url, stream=True) as r:
        r.raise_for_status() # Check for HTTP errors
        with open('updateFile.zip', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    print("Starting stage 3...")
    os.system("bash applyUpdate.sh &")
if __name__ == "__main__":
    main()