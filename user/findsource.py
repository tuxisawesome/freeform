import sys
from time import sleep
import os

def find_source(friendlyname):
    #Deprecated
    pass


def find_source_line(friendlyname):
    os.system(f"/tyr/tyr install {friendlyname} -y")
    print("installed.")