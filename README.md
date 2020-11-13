# Flasketvj

Flask Dashboard built with Python to control videomapping on raspberry pi

## DOWNLOAD

I made a image with all the setupworking
USER:
PI
PASSWORD:
pimapperrulez

just make an hotspot from yout mobile phone with this data:

SSID:
flasketvjnetwork
Password:
pimapperrulez
(!CHANGE IT!)

My country is IT so you will have to update accordingly to your location:

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Connect to the hostname of you raspberrypi with your browser
frontend:
http://mapperbox0.local
shell:
http://mapperbox0.local:4200

or Rpi Ip Address (spoiler: you can see it in your mobile)

to interact with the mapping click on the mapping button.

I addeded some handy stuff like copiyng sources from usb with a button, having a shell open in the browser,have fun looking around!
I made the interface as funny as possible. Hope you enjoy it.

##TODO:

- import and export config from web interface
- upload and download sources from web interface
- what else..

## Base setup for building this was:

starting from the image of the awesome ofxPimapper(raspbian stretch)
https://ofxpimapper.com/
https://gitlab.com/kriwkrow/pimapper/-/jobs/280309100/artifacts/raw/PiMapper_v1.2.0.zip
burn it to sd
git clone this repo to /home/pi/ beside the ofx folder

## !!!SWITCH KEYBOARD TO AMERICAN US VIA RASPI-CONFIG !!!

`sudo raspi-config > Localisation Options >Change Keyboard Layout > other > Generic 105-key (Intl) PC > English US`

## Install dependencies

`sudo apt-get install python3 python3-pip python3-flask python3-dev nginx`

`sudo pip3 install flask keyboard RPi.GPIO flask-ngrok gunicorn uwsgi`

## Installing Python3.6 on a Raspberry Pi becouse i want to try with ngrok forwarding the mapper frontend
#
`sudo apt-get install python3-dev libffi-dev libssl-dev -y

sudo apt-get install python3-dev libffi-dev libssl-dev -y
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tar.xz
tar xJf Python-3.6.3.tar.xz
cd Python-3.6.3
./configure
make
sudo make install
sudo pip3 install --upgrade pip
which python3.6
sudo nano ~/.bashrc
alias python3='/usr/local/bin/python3.6'
source ~/.bashrc
python -V
`

## configure nginx
https://www.e-tinkers.com/2018/08/how-to-properly-host-flask-application-with-nginx-and-guincorn/

## Getting started:

- **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running:

  `sudo apt-get install python3-flask`

## Spinning the in development:

- **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running:

  `cd flasketvj/`
  `sudo python3 app.py`

## [Locally] Accessing the Dashboard:

- Since the servlet is running locally, you can access the dashboard by navigating to **http://mapperbox0.local** through your web browser

## [Remotely] Accessing the Dashboard:not implemented yet
<!-- ## What i learned

- what really are stdin stdout
- Each file in Linux has a corresponding File Descriptor associated with it
- The keyboard is the standard input device while your screen is the standard output device
- ">" is the output redirection operator. ">>" appends output to an existing file
- "<" is the input redirection operator
- ">&"re-directs output of one file to another.
- You can re-direct error using its corresponding File Descriptor 2.
  https://www.guru99.com/linux-redirection.html -->

<!-- ## TODO
-switch access point - client - no wifi with Gpio buttons
 https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/158-raspberry-pi-auto-wifi-hotspot-switch-direct-connection -->
