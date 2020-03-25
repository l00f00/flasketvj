from flask import Flask, render_template, request
import os
import subprocess
import keyboard

app = Flask(__name__)


def mapperInfo():
    info = ''
    return info


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
def getMemoryUsage(lineNumber):
    response = os.popen('free -m').readlines()
    return response[lineNumber].split()

def checked():
    checked=''
    return checked


# function that returns how long the raspberry pi has been running
def getUptime():
    response = os.popen('cat /proc/uptime').readline().split(
    )  # reads the response as an array of strings for each line
    minutes = int(float(response[0]) / 60)
    time = [0, 0, 0]
    time[0] = int(minutes / 24 / 60)  # get days
    time[1] = int(minutes / 60 % 24)  # get hours
    time[2] = minutes % 60  # get minutes
    return time


# function that returns disk usage
def getDiskUsage(lineNumber):
    response = os.popen('df -h').readlines(
    )  # reads the response as an array of strings for each line
    return response[lineNumber].split(
    )  # splits a specific line into an array of words based on lineNumber


# function that returns cpu temperature in fahrenheit
def getFahrenheit():
    response = os.popen('vcgencmd measure_temp').readline(
    )  # get the response from running the command 'vcgencmd measure_temp'
    celsius = float(response.replace("temp=", "").replace(
        "'C\n", ""))  # get rid of 'temp=' and ''C'
    fahrenheit = round(
        ((celsius * (9 / 5)) + 32),
        1)  # convert from fahrenheit to celsius rounded to one decimal place
    return fahrenheit


# function that returns cpu temperature in celsius
def getCelsius():
    response = os.popen('vcgencmd measure_temp').readline(
    )  # get the response from running the command 'vcgencmd measure_temp'
    celsius = float(response.replace("temp=", "").replace(
        "'C\n", ""))  # get rid of 'temp=' and ''C'
    celsius = round(celsius, 1)  # celsius rounded to one decimal place
    return celsius

# def clearconsole():
#     response = os.system(
#         "sudo killall -u root -SIGKILL example_basic && reset")
#     info = 'Mapper Killed'
#     return info

# Keyboard Mapper
# def save_mapper():
#     mapperSaver = keyboard.write('ss')
#     return "saved"


@app.route('/')
def index():
    return render_template(
        'index.html',
        fahrenheit=getFahrenheit(),
        celsius=getCelsius(),
        diskUsageHeader=getDiskUsage(0),  # array for Disk Usage <th>
        diskUsageInfo=getDiskUsage(1),  # array for Disk Usage <td>
        upTime=getUptime(),  # how long the raspberry pi has been running
        memoryUsageHeader=getMemoryUsage(0),  # array for Memory Usage <th>
        memoryUsageInfo=getMemoryUsage(1),  # array for Memory Usage <td>
        memoryUsePercentage=round(
            float(getMemoryUsage(1)[2]) / float(getMemoryUsage(1)[1]), 4) *
        100,  # percentage of used Memory
        #                           userName=getUserName(),
        ipAddress=getIpAddress()[0],
        hostname=getHostname()[0],
        processInfo=getProcessInfo())

@app.route('/mapper', methods=['POST', 'GET'])
def mapper():
    info = 'start mapping'
    return render_template('mapper.html',
                           ipAddress=getIpAddress()[0],
                           hostname=getHostname()[0],
                           infoText=info)  # admin mapper


@app.route('/clear_console')
def clearconsole():
    keyboard.write('reset')
    #os.system("sudo reset")
    info = 'Mapper Killed & CLI CLEARED'
    return render_template('mapper.html',
                           ipAddress=getIpAddress()[0],
                           hostname=getHostname()[0],
                           infoText=info)  # admin mapper


#RUN MAPPER
@app.route('/mapper_run')
def turn_on():
    os.popen(
        "/home/pi/ofx/addons/ofxPiMapper/example_basic/./bin/example_basic -f >/dev/null 2>&1"
    )
    info = 'Mapper Running'
    return render_template('mapper.html', infoText=info)


#Kill Mapper
@app.route('/mapper_kill')
def turn_off():
    os.system("sudo killall -u root -SIGKILL example_basic")
    info = 'Mapper Killed'
    return render_template('mapper.html', infoText=info)


# Key	Function
# def some_view():
#     return render_template('template.html', checked='home')

# 1	Presentation mode
@app.route('/present_mode')
def present_mode():
    keyboard.write('1')
    info = 'Presentation mode'
    return render_template('mapper.html', infoText=info,checked='present')


# 2	Texture editing mode
@app.route('/texture_mode')
def texture_mode():
    keyboard.write('2')
    info = 'Texture Editing Mode'
    return render_template('mapper.html', infoText=info,checked='texture')


# 3	Projection mapping mode, use this to select a surface first
@app.route('/mapping_mode')
def mapping_mode():
    keyboard.write('3')
    info = 'Projection mapping mode'
    return render_template('mapper.html', infoText=info,checked='mapping')


# 4	Source selection mode
@app.route('/source_selection_mode')
def source_selection_mode():
    keyboard.write('4')
    info = 'Source selection mode'
    return render_template('mapper.html', infoText=info,checked='source')


# i	Show info Controls
@app.route('/show_controls')
def show_controls():
    keyboard.write('i')
    info = 'Show info Controls'
    return render_template('mapper.html', infoText=info,checked='info')


# t	Add triangle surface
@app.route('/add_triangle')
def add_triangle():
    keyboard.write('t')
    info = 'Addeded Triangle'
    return render_template('mapper.html', infoText=info,checked='mapping')


# q	Add quad surface
@app.route('/add_quad')
def add_quad():
    keyboard.write('q')
    info = 'Addeded Quad'
    return render_template('mapper.html', infoText=info,checked='mapping')


# g	Add grid warp surface
@app.route('/add_grid')
def add_grid():
    keyboard.write('g')
    info = 'Addeded Grid Warp'
    return render_template('mapper.html', infoText=info,checked='mapping')


# c	Add circle surface
@app.route('/add_circle')
def add_circle():
    keyboard.write('c')
    info = 'Add circle surface'
    return render_template('mapper.html', infoText=info,checked='mapping')


# d	duplicate selected surface
@app.route('/duplicate')
def duplicate():
    keyboard.write('d')
    info = 'Duplicated Selected Surface'
    return render_template('mapper.html', infoText=info,checked='mapping')


# +	Scale surface up
@app.route('/scale_up')
def scale_up():
    keyboard.write('+')
    info = 'Scaled surface up +'
    return render_template('mapper.html', infoText=info,checked='mapping')


# -	Scale surface down
#NOT WORKING
@app.route('/scale_down')
def scale_down():
    keyboard.write('-')
    info = 'Scale surface down -'
    return render_template('mapper.html', infoText=info,checked='mapping')


# p	toggle perspective warping (quad surfaces only)
@app.route('/toggle_perspective')
def toggle_perspective():
    keyboard.write('p')
    info = 'Toggle perspective warping<br/>(quad surfaces only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# ]	add columns to grid surface (grid warp surfaces only)
@app.route('/add_columns')
def add_columns():
    keyboard.press_and_release(']')
    info = 'add columns to grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# [	remove columns from grid surface (grid warp surfaces only)
@app.route('/remove_columns')
def remove_columns():
    keyboard.press_and_release('[')
    info = 'remove columns from grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# }	add rows to grid surface (grid warp surfaces only)
@app.route('/add_rows')
def add_rows():
    keyboard.write('}')
    info = 'add rows to grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# {	remove rows from grid surface (grid warp surfaces only)
@app.route('/remove_rows')
def remove_rows():
    keyboard.write('{')
    info = 'remove rows from grid surface<br/>(grid warp surfaces only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# .	select next surface (projection mapping mode only)
@app.route('/next_surface')
def next_surface():
    keyboard.write('.')
    info = 'select next surface<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# ,	select previous surface (projection mapping mode only)
@app.route('/previous_surface')
def previous_surface():
    keyboard.write(',')
    info = 'select previous surface<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# >	select next vertex
@app.route('/next_vertex')
def next_vertex():
    keyboard.write('>')
    info = 'select next vertex<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# <	select previous vertex
@app.route('/previous_vertex')
def previous_vertex():
    keyboard.write('<')
    info = 'previous next vertex<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# 0	Move selected surface one layer up


@app.route('/layer_up')
def layer_up():
    keyboard.write('0')
    info = 'Move selected surface one layer up<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# 9	Move selected surface one layer down


@app.route('/layer_down')
def layer_down():
    keyboard.write('9')
    info = 'Move selected surface one layer down<br/>(projection mapping mode only)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# s	Save composition
@app.route('/mapper_save')
def save_mapper():
    keyboard.write('ss')
    info = 'Saved'
    return render_template('mapper.html', infoText=info,checked='save')


# l	Hide/show layer panel
@app.route('/layer_panel')
def layer_panel():
    keyboard.write('l')
    info = 'Hide/show layer panel'
    return render_template('mapper.html', infoText=info,checked='mapping')


# z	Undo
@app.route('/Undo')
def Undo():
    keyboard.write('z')
    info = 'Undo'
    return render_template('mapper.html', infoText=info,checked='undo')


# rbt	Reboot (Raspberry Pi only)
@app.route('/reboot')
def reboot():
    keyboard.write('s')
    keyboard.write('rbt')
    info = 'reboooootin wait up!'
    return render_template('mapper.html', infoText=info,checked='mapping')


# sdn	Shutdown (Raspberry Pi only)
@app.route('/shutdown')
def shudown():
    keyboard.write('s')
    keyboard.write('sdn')
    info = 'Saving and Shutting Down!'
    return render_template('mapper.html', infoText=info)


# new	Clear composition (remove all surfaces)
@app.route('/newcomp')
def newcomp():
    keyboard.write('new')
    info = 'Clear composition<br/>(remove all surfaces)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# ext	Exit application and return to command line
@app.route('/ext')
def ext():
    keyboard.write('ext')
    info = 'Exit application and return to command line'
    return render_template('mapper.html', infoText=info)


# BACKSPACE ('' via SSH)	Delete surface.
@app.route('/delete')
def BACKSPACE():
    keyboard.send('backspace')
    info = 'Delete surface'
    return render_template('mapper.html', infoText=info,checked='mapping')


# SPACE	Toggle pause for video sources (texture and projection mapping modes)
@app.route('/pause')
def SPACE():
    keyboard.send('space')
    info = 'Pause'
    return render_template('mapper.html', infoText=info,checked='mapping')


# TAB	Select next source (no need to use the source selection interface)
@app.route('/next_source')
def next_source():
    keyboard.send('tab')
    info = 'Select next source<br/>(no need to use the source selection interface)'
    return render_template('mapper.html', infoText=info,checked='mapping')


# Arrow keys	Move selection. If no surface is selected in the projection mapping mode, all surfaces are moved.
@app.route('/arrow_up')
def arrow_up():
    keyboard.send('up')
    info = 'arrow up'
    return render_template('mapper.html', infoText=info,checked='mapping')


@app.route('/arrow_down')
def arrow_down():
    keyboard.send('down')
    info = 'arrow down'
    return render_template('mapper.html', infoText=info,checked='mapping')


@app.route('/arrow_left')
def arrow_left():
    keyboard.send('left')
    info = 'arrow left'
    return render_template('mapper.html', infoText=info,checked='mapping')


@app.route('/arrow_right')
def arrow_right():
    keyboard.send('right')
    info = 'arrow right'
    return render_template('mapper.html', infoText=info,checked='mapping')


# /	Toggle 1px/10px steps for keyboard moves on Raspberry Pi
@app.route('/accuracy')
def accuracy():
    keyboard.send('/')
    info = 'Toggle 1px/10px steps for keyboard moves on Raspberry Pi'
    return render_template('mapper.html', infoText=info,checked='mapping')


if __name__ == '__main__':
    app.run(debug=checked, host='mapperbox0.local', port=80)
