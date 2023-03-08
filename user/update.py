# Update Wrapper

import os
import sys
from time import sleep
os.system("rm -rf client.zip")
os.system("curl https://raw.githubusercontent.com/tuxisawesome/freeform/main/release/client.zip > client.zip")
sleep(5)
print("Waiting 5 seconds to make sure the server stopped...")
os.system("rm -rf client")
os.system("unzip client.zip")
print("Done!")
os.system("reboot")