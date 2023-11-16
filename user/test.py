import sys
import os
import findsource
if not sys.argv[1]:
    name = "none"
name = sys.argv[1]
def run(name):
    findsource.find_source(name)
run(name)