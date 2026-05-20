#!/bin/bash

killall python
killall python3
echo "Applying update now... stage 3"
rm -rf systemData/*
unzip updateFile.zip -d systemData
echo "Update applied..."
