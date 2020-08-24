#!/bin/bash
sudo apt-get update
sudo apt-get install python3-venv python3-pip python3-setuptools -y
python3 -m venv env
pip3 install pip setuptools wheel --upgrade
pip3 install -r requirements.txt
