# Flasketvj!

Flask Dashboard built with Python to control a videomapping on raspberry pi, this is just a frontend for the awesome [ofxPimapper](https://github.com/kr15h/ofxPiMapper)

<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/43296799/123779115-1d39ef80-d8d2-11eb-9873-cf91a60b049f.gif" alt="2" width = 500px ></td>
    <td><img src="https://user-images.githubusercontent.com/43296799/123779302-53776f00-d8d2-11eb-8982-1b02fa90dc2e.gif"  alt="1" width = 500px ></td>
  </tr>
<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/43296799/123778286-3d1ce380-d8d1-11eb-911a-28a433ac2f30.jpg" alt="2" width = 200px ></td>
    <td><img src="https://user-images.githubusercontent.com/43296799/123771764-9e41b880-d8cb-11eb-8d6e-103af303b7d5.jpg"  alt="1" width = 200px ></td>
    <td><img src="https://user-images.githubusercontent.com/43296799/123771794-a39f0300-d8cb-11eb-9e69-8b7034a3a0b0.jpg"  alt="1" width = 200px></td> 
  </tr>
   <tr>
     <td><img src="https://user-images.githubusercontent.com/43296799/123771682-8b2ee880-d8cb-11eb-9610-4809c35aef11.jpg" alt="2" width = 200px height = 400px ></td>
     <td><img src="https://user-images.githubusercontent.com/43296799/123771688-8bc77f00-d8cb-11eb-881a-cc70e7eae2e9.jpg"  alt="1" width = 200px height = 400px ></td>
     <td><img src="https://user-images.githubusercontent.com/43296799/123771689-8c601580-d8cb-11eb-85dc-8400a170a64a.jpg" alt="2" width = 200px height = 400px ></td>
     <td><img src="https://user-images.githubusercontent.com/43296799/123771692-8c601580-d8cb-11eb-931b-1247d6b12a3f.jpg"  alt="1" width = 200px height = 400px ></td>
     <td><img src="https://user-images.githubusercontent.com/43296799/123771694-8c601580-d8cb-11eb-8efe-acc794dfed07.jpg" alt="2" width = 200px height = 400px ></td>
  </tr>
</table>

## DOWNLOAD
[Ready to burn Raspberrypi image, Download from Mega](https://mega.nz/file/eshGwSyK#0_N1_IYLLxQZjV0zzlMHdip_RCP_k2hWmYU5cvd5wi8)

`USER:
pi
PASSWORD:
pimapperrulez`

just make an hotspot from yout mobile phone with this data:

`SSID:
flasketvjnetwork
Password:
pimapperrulez
(!CHANGE IT!)`

My country is IT so you will have to update accordingly to your location:

`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

Connect to the hostname of you raspberrypi with your browser
frontend:
http://mapperbox0.local
shell:
http://mapperbox0.local:4200

or Rpi Ip Address (spoiler: you can see it in your mobile)

<details>
  <summary>So many buttons</summary>
  
  The interface is divided in 4 label, mapping(on the left),sliceselection,source selection, and play. Just like ofxPimapper.
  In fact this little frontend only mimics Pimapper in all it's functionality giving the possibility to do the mapping from your mobile phone or pc.
  I found it easier that having to attach mouse and keyboard to the raspberry itself.
  It also autosaves every time you pass from one label to another.Very handy.
  This is possible by emulating the keyboard trough python and basically writing the py mapper commands to the console, under the hood there is noting more than flask
  and some script to tie it all up.
  I have an issue with overflowing text appearing in the little screen on top causing the slide down of the buttons grid, i'll fix it in the next rel.
  
  
  To interact with the mapping click on the mapping button.

  I addeded some handy stuff like copiyng sources from usb with a button, having a shell open in the browser,have fun looking around!
  </details>

I made the interface as funny as possible.
Enjoy it.

<details>
  <summary>How it's done</summary>

  ###### Base for building this was:

    starting from the image of the awesome ofxPimapper(raspbian stretch)
    https://ofxpimapper.com/
    https://gitlab.com/kriwkrow/pimapper/-/jobs/280309100/artifacts/raw/PiMapper_v1.2.0.zip
    burn it to sd
    git clone this repo to /home/pi/ beside the ofx folder

    ###### !!!SWITCH KEYBOARD TO AMERICAN US VIA RASPI-CONFIG !!!

    `sudo raspi-config > Localisation Options >Change Keyboard Layout > other > Generic 105-key (Intl) PC > English US`

    ###### Install dependencies

    `sudo apt-get install python3 python3-pip python3-flask python3-dev nginx`

    `sudo pip3 install flask keyboard RPi.GPIO flask-ngrok gunicorn uwsgi`

    ###### Installing Python3.6 on a Raspberry Pi because i want to try with ngrok forwarding the mapper frontend and it worked
    ###### Add your keys for ngrok

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

    ###### configure nginx
    `
    https://www.e-tinkers.com/2018/08/how-to-properly-host-flask-application-with-nginx-and-guincorn/
    `

    ###### Getting started:

    - **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running:

      `sudo apt-get install python3-flask`

    ###### Spinning the in development:

    - **app.py** is our servlet, which runs using Flask (http://flask.pocoo.org/). Install it by running:

      `cd flasketvj/`
      `sudo python3 app.py`

    ###### [Locally] Accessing the Dashboard:

    - Since the servlet is running locally, you can access the dashboard by navigating to **http://mapperbox0.local** through your web browser

    ###### What i learned

    - what really are stdin stdout
    - ">" is the output redirection operator. ">>" appends output to an existing file
    - "<" is the input redirection operator
    - ">&"re-directs output of one file to another.
    - You can re-direct error using its corresponding File Descriptor 2.
      https://www.guru99.com/linux-redirection.html 
</details>
    #TODO:

    - add basic authentication
    - remotely accessing the dashboard
    - import and export config from web interface
    - upload and download sources from web interface
    - what else..
    -switch access point - client - no wifi with Gpio buttons
     https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/158-raspberry-pi-auto-wifi-hotspot-switch-direct-connection
