# Flasketvj
Flask Dashboard built with Python to control videomapping stuff on raspberry pi
# Base setup
start from the image of the awsome ofxPimapper(raspbian stretch)
https://ofxpimapper.com/
https://gitlab.com/kriwkrow/pimapper/-/jobs/280309100/artifacts/raw/PiMapper_v1.2.0.zip
burn it to sd
git clone this repo to /home/pi/ besite the ofx folder
## Install dependencies ##
`sudo apt-get install python3 python3-pip python3-flask`

TODO:add dependencies from pip [keyboard subprocess etc]

## Getting started: ##
* **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running: 

  `sudo apt-get install python3-flask`

## Spinning the shit in development: ##
* **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running: 

  `cd flasketvj/`
  `sudo python3 app.py`

<!-- ## Starting the servlet: ##
* change to the **rpi-status-monitor** directory
* From the command line:

  `sudo python3 app.py`
* My servlet is running through crontab on my raspberry pi. It runs the program every time the rpi restarts.
  For info on how to set up crontab, follow this link: https://www.raspberrypi.org/documentation/linux/usage/cron.md
  
  `@reboot sudo python3 rpi-status-monitor/app.py &` -->
  
## [Locally] Accessing the Dashboard: ##
* Since the servlet is running locally, you can access the dashboard by navigating to **http://mapperbox0.local** through your web browser

## [Remotely] Accessing the Dashboard: ##
