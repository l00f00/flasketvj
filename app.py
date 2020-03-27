# from flask import Flask, render_template, request, make_response
from flask import *
import os
import subprocess
import keyboard
import raspi

app = Flask(__name__)
# import raspi.pi for GPIO interaction
raspi = raspi.Raspi()

#  mapper mini display
def mapperInfo():
    info = ''
    return info

# information about running process
def getProcessInfo():
    response = os.popen('top -b -n1').readlines()
    return response[1].split()


#function that returns IP Address
def getIpAddress():
    response = os.popen('hostname -I').readline()
    return response.split()


#function that returns hostname
def getHostname():
    response = os.popen('hostname').readline()
    return response.split()


# function that returns username
#def getUserName():
#    response = os.popen('users').readline()
#    return response


# function that returns memory usage in MBs
# def getMemoryUsage(lineNumber):
#     response = os.popen('free -m').readlines()
#     return response[lineNumber].split()


# # function that returns how long the raspberry pi has been running
# def getUptime():
#     response = os.popen('cat /proc/uptime').readline().split(
#     )  # reads the response as an array of strings for each line
#     minutes = int(float(response[0]) / 60)
#     time = [0, 0, 0]
#     time[0] = int(minutes / 24 / 60)  # get days
#     time[1] = int(minutes / 60 % 24)  # get hours
#     time[2] = minutes % 60  # get minutes
#     return time


# # function that returns disk usage
# def getDiskUsage(lineNumber):
#     response = os.popen('df -h').readlines(
#     )  # reads the response as an array of strings for each line
#     return response[lineNumber].split(
#     )  # splits a specific line into an array of words based on lineNumber


# # function that returns cpu temperature in fahrenheit
# def getFahrenheit():
#     response = os.popen('vcgencmd measure_temp').readline(
#     )  # get the response from running the command 'vcgencmd measure_temp'
#     celsius = float(response.replace("temp=", "").replace(
#         "'C\n", ""))  # get rid of 'temp=' and ''C'
#     fahrenheit = round(
#         ((celsius * (9 / 5)) + 32),
#         1)  # convert from fahrenheit to celsius rounded to one decimal place
#     return fahrenheit


# # function that returns cpu temperature in celsius
# def getCelsius():
#     response = os.popen('vcgencmd measure_temp').readline(
#     )  # get the response from running the command 'vcgencmd measure_temp'
#     celsius = float(response.replace("temp=", "").replace(
#         "'C\n", ""))  # get rid of 'temp=' and ''C'
#     celsius = round(celsius, 1)  # celsius rounded to one decimal place
#     return celsius

# def clearconsole():
#     response = os.system(
#         "sudo killall -u root -SIGKILL example_basic && reset")
#     info = 'Mapper Killed'
#     return info

# Keyboard Mapper
# def save_mapper():
#     mapperSaver = keyboard.write('ss')
#    return "saved"

# function that returns infoText in monitor
def getinfoText():
    infoText=''
    return infoText

@app.route('/')
def index():
    infoText='this is the monitor'
    return render_template(
        'index.html',
        ipAddress=getIpAddress()[0],
        hostname=getHostname()[0],
        infoText=infoText)

# Change LED value POST request.
@app.route("/change_led_status/<int:status>", methods=['POST'])
def change_led_status(status):
  # Check the value of the parameter
  if status == 0:
    raspi.change_led(False)
  elif status == 1:
    raspi.change_led(True)
  else:
    return ('Error', 500)
  return ('', 200)

@app.route('/mapper', methods=['POST', 'GET'])
def mapper():
    info = 'start mapping'
    return render_template('mapper.html',
                           ipAddress=getIpAddress()[0],
                           hostname=getHostname()[0],
                           infoText=info)
# return make_response('it worked!', 200, headers)
#RUN MAPPER
@app.route('/mapper/turn_on/', methods=['POST'])
def turn_on():
    os.popen(
        "/home/pi/ofx/addons/ofxPiMapper/example_basic/./bin/example_basic -f >/dev/null 2>&1"
    )
    infoText = 'Mapper Running'
    return (infoText, 200)


#Kill Mapper
@app.route('/mapper/turn_off/', methods=['POST'])
def turn_off():
    os.system("sudo killall -u root -SIGKILL example_basic")
    infoText = 'Mapper Killed'
    return (infoText, 200)

# clearconsole
@app.route('/mapper/clearconsole/', methods=['POST'])
def clearconsole():
    keyboard.write('reset')
    keyboard.send('enter')
    #os.system("sudo reset")
    infoText = 'Mapper Killed & CLI CLEARED'
    return (infoText, 200)

# ext	Exit application and return to command line
@app.route('/mapper/ext/', methods=['POST'])
def ext():
    keyboard.write('ext')
    # os.system("sudo killall -u root -SIGKILL example_basic")
    info = 'Exit application and return to command line(while in mappingmode)'
    return (infoText, 200)

# rbt	Reboot (Raspberry Pi only)

def reboot():
    keyboard.write('s')
    keyboard.write('rbt')
    # os.system("sudo reboot now")
    info = 'reboooootin wait up!'
    return (infoText, 200)

# sdn	Shutdown (Raspberry Pi only)
@app.route('/mapper/shudown/', methods=['POST'])
def shudown():
    keyboard.write('s')
    keyboard.write('sdn')
    # os.system("sudo shutdown now")
    info = 'Saving and Shutting Down!'
    return (infoText, 200)
#################MapperModes####################
# 1	Presentation mode
@app.route('/present_mode')
def present_mode():
    keyboard.write('1')
    info = 'Presentation mode'
    return (infoText, 200)


# 2	Texture editing mode
@app.route('/texture_mode')
def texture_mode():
    keyboard.write('2')
    info = 'Texture Editing Mode'
    return render_template('mapper.html', infoText=info)


# 3	Projection mapping mode, use this to select a surface first
@app.route('/mapping_mode')
def mapping_mode():
    keyboard.write('3')
    info = 'Projection mapping mode'
    return render_template('mapper.html', infoText=info)


# 4	Source selection mode
@app.route('/source_selection_mode')
def source_selection_mode():
    keyboard.write('4')
    info = 'Source selection mode'
    return render_template('mapper.html', infoText=info)


# i	Show info Controls
@app.route('/show_controls')
def show_controls():
    keyboard.write('i')
    info = 'Show info Controls'
    return render_template('mapper.html', infoText=info)


# t	Add triangle surface
@app.route('/add_triangle')
def add_triangle():
    keyboard.write('t')
    info = 'Addeded Triangle'
    return render_template('mapper.html', infoText=info)


# q	Add quad surface
@app.route('/add_quad')
def add_quad():
    keyboard.write('q')
    info = 'Addeded Quad'
    return render_template('mapper.html', infoText=info)


# g	Add grid warp surface
@app.route('/add_grid')
def add_grid():
    keyboard.write('g')
    info = 'Addeded Grid Warp'
    return render_template('mapper.html', infoText=info)


# c	Add circle surface
@app.route('/add_circle')
def add_circle():
    keyboard.write('c')
    info = 'Add circle surface'
    return render_template('mapper.html', infoText=info)


# d	duplicate selected surface
@app.route('/duplicate')
def duplicate():
    keyboard.write('d')
    info = 'Duplicated Selected Surface'
    return render_template('mapper.html', infoText=info)


# +	Scale surface up
@app.route('/scale_up')
def scale_up():
    keyboard.write('+')
    info = 'Scaled surface up +'
    return render_template('mapper.html', infoText=info)


# -	Scale surface down
#NOT WORKING
@app.route('/scale_down')
def scale_down():
    keyboard.write('-')
    info = 'Scale surface down -'
    return render_template('mapper.html', infoText=info)


# p	toggle perspective warping (quad surfaces only)
@app.route('/toggle_perspective')
def toggle_perspective():
    keyboard.write('p')
    info = 'Toggle perspective warping<br/>(quad surfaces only)'
    return render_template('mapper.html', infoText=info)


# ]	add columns to grid surface (grid warp surfaces only)
@app.route('/add_columns')
def add_columns():
    keyboard.press_and_release(']')
    info = 'add columns to grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info)


# [	remove columns from grid surface (grid warp surfaces only)
@app.route('/remove_columns')
def remove_columns():
    keyboard.press_and_release('[')
    info = 'remove columns from grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info)


# }	add rows to grid surface (grid warp surfaces only)
@app.route('/add_rows')
def add_rows():
    keyboard.write('}')
    info = 'add rows to grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info)


# {	remove rows from grid surface (grid warp surfaces only)
@app.route('/remove_rows')
def remove_rows():
    keyboard.write('{')
    info = 'remove rows from grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info)


# .	select next surface (projection mapping mode only)
@app.route('/next_surface')
def next_surface():
    keyboard.write('.')
    info = 'select next surface<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info)


# ,	select previous surface (projection mapping mode only)
@app.route('/previous_surface')
def previous_surface():
    keyboard.write(',')
    info = 'select previous surface<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info)


# >	select next vertex
@app.route('/next_vertex')
def next_vertex():
    keyboard.write('>')
    info = 'select next vertex<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info)


# <	select previous vertex
@app.route('/previous_vertex')
def previous_vertex():
    keyboard.write('<')
    info = 'previous next vertex<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info)


# 0	Move selected surface one layer up


@app.route('/layer_up')
def layer_up():
    keyboard.write('0')
    info = 'Move selected surface one layer up<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info)


# 9	Move selected surface one layer down


@app.route('/layer_down')
def layer_down():
    keyboard.write('9')
    info = 'Move selected surface one layer down<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info)


# s	Save composition
@app.route('/mapper_save')
def save_mapper():
    keyboard.write('ss')
    info = 'Saved'
    return render_template('mapper.html', infoText=info)


# l	Hide/show layer panel
@app.route('/layer_panel')
def layer_panel():
    keyboard.write('l')
    info = 'Hide/show layer panel'
    return render_template('mapper.html', infoText=info)


# z	Undo
@app.route('/Undo')
def Undo():
    keyboard.write('z')
    info = 'Undo'
    return render_template('mapper.html', infoText=info)



# new	Clear composition (remove all surfaces)
@app.route('/newcomp')
def newcomp():
    keyboard.write('new')
    info = 'Clear composition<br/>(remove all surfaces)'
    return render_template('mapper.html', infoText=info)


# BACKSPACE ('' via SSH)	Delete surface.
@app.route('/delete')
def BACKSPACE():
    keyboard.send('backspace')
    info = 'Delete surface'
    return render_template('mapper.html', infoText=info)


# SPACE	Toggle pause for video sources (texture and projection mapping modes)
@app.route('/pause')
def SPACE():
    keyboard.send('space')
    info = 'Pause'
    return render_template('mapper.html', infoText=info)


# TAB	Select next source (no need to use the source selection interface)
@app.route('/next_source')
def next_source():
    keyboard.send('tab')
    info = 'Select next source<br/>(no need to use the source selection interface)'
    return render_template('mapper.html', infoText=info)


# Arrow keys	Move selection. If no surface is selected in the projection mapping mode, all surfaces are moved.
@app.route('/arrow_up')
def arrow_up():
    keyboard.send('up')
    info = 'arrow up'
    return render_template('mapper.html', infoText=info)


@app.route('/arrow_down')
def arrow_down():
    keyboard.send('down')
    info = 'arrow down'
    return render_template('mapper.html', infoText=info)


@app.route('/arrow_left')
def arrow_left():
    keyboard.send('left')
    info = 'arrow left'
    return render_template('mapper.html', infoText=info)


@app.route('/arrow_right')
def arrow_right():
    keyboard.send('right')
    info = 'arrow right'
    return render_template('mapper.html', infoText=info)


# /	Toggle 1px/10px steps for keyboard moves on Raspberry Pi
@app.route('/accuracy')
def accuracy():
    keyboard.send('/')
    info = 'Toggle 1px/10px steps for keyboard moves on Raspberry Pi'
    return render_template('mapper.html', infoText=info)


if __name__ == '__main__':
    app.run(debug=True, host='mapperbox0.local', port=80)
