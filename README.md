# rpi-status-monitor
Flask Dashboard built with Python that displays status information about the raspberry pi

## Getting started: ##
* **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running: 

  `sudo apt-get install python3-flask`

## Starting the servlet: ##
* change to the **rpi-status-monitor** directory
* From the command line:

  `sudo python3 app.py`
* My servlet is running through crontab on my raspberry pi. It runs the program every time the rpi restarts.
  For info on how to set up crontab, follow this link: https://www.raspberrypi.org/documentation/linux/usage/cron.md
  
  `@reboot sudo python3 rpi-status-monitor/app.py &`
  
## [Locally] Accessing the Dashboard: ##
* Since the servlet is running locally, you can access the dashboard by navigating to **https://127.0.0.1** through your pi's web browser

## [Remotely] Accessing the Dashboard: ##
