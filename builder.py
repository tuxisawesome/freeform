from os import system
import sys


# Step 1: Zip the system
system("zip -r client.zip client")

# Step 2: Put in release folder
system("mv client.zip ../release")