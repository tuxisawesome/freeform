import os
import sys

# os.system("pip3 install flask")
# os.system("pip3 install requests")

with open('./version.txt','r') as file:
    softversion = file.read()

print(softversion)
print("FreeForm has been installed.")