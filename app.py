# from flask import Flask, render_template, request, make_response
from flask import *
import os

# import subprocess
import keyboard

# import raspi
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# import raspi.pi for GPIO interaction
# raspi = raspi.Raspi()
# run_with_ngrok(app)  # Start ngrok when app is run

# information about running process
def getProcessInfo():
    response = os.popen("top -b -n1").readlines()
    return response[1].split()


# function that returns IP Address
def getIpAddress():
    response = os.popen("hostname -I").readline()
    return response.split()


# function that returns hostname
def getHostname():
    response = os.popen("hostname").readline()
    return response.split()


# function that returns username
# def getUserName():
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
#  mapper mini display

# def mapperInfo(infoText):
#     return infoText
#   def read_sensor(self):
#     return GPIO.input(SENSOR_PIN)


@app.route("/")
def index():
    infoText = "mapper home"
    return render_template("index.html")

    # return render_template(
    #     "index.html", ipAddress=getIpAddress()[0], hostname=getHostname()[0]
    # )


# # Change LED value POST request.
# @app.route("/change_led_status/<int:status>", methods=["POST"])
# def change_led_status(status):
#     # Check the value of the parameter
#     if status == 0:
#         raspi.change_led(False)
#     elif status == 1:
#         raspi.change_led(True)
#     else:
#         return ("Error", 500)
#     return ("", 200)


# @app.route('/mapper', methods=['POST', 'GET'])
# def mapper():
#     infoText = 'start mapping'
#     return render_template('mapper.html',
#                            ipAddress=getIpAddress()[0],
#                            hostname=getHostname()[0],
#                            infoText=mapperInfo(infoText))
# return make_response('it worked!', 200, headers)

# RUN MAPPER
@app.route("/mapper/turn_on/", methods=["POST", "GET"])
def turn_on():
    os.popen(
        "/home/pi/ofx/addons/ofxPiMapper/example_basic/./bin/example_basic -f >/dev/null 2>&1"
    )
    return ("", 200)


# Kill Mapper
@app.route("/mapper/turn_off/", methods=["POST"])
def turn_off():
    os.system("sudo killall -u root -SIGKILL example_basic")
    return ("", 200)


# clearconsole
@app.route("/mapper/clearconsole/", methods=["POST"])
def clearconsole():
    keyboard.write("reset")
    keyboard.send("enter")
    # os.system("sudo reset")
    return ("", 200)


# ext	Exit application and return to command line
@app.route("/mapper/ext/", methods=["POST"])
def ext():
    keyboard.write("ext")
    # os.system("sudo killall -u root -SIGKILL example_basic")
    return ("", 200)


# rbt	Reboot (Raspberry Pi only)
@app.route("/mapper/reboot/", methods=["POST"])
def reboot():
    keyboard.write("s")
    keyboard.write("rbt")
    # os.system("sudo reboot now")
    return ("", 200)


# sdn	Shutdown (Raspberry Pi only)
@app.route("/mapper/shutdown/", methods=["POST"])
def shutdown():
    keyboard.write("s")
    keyboard.write("sdn")
    # os.system("sudo shutdown now")
    return ("", 200)


#################MapperModes####################
# 1	Presentation mode
@app.route("/mapper/present_mode/", methods=["POST"])
def present_mode():
    keyboard.write("1")
    info = "Presentation mode"
    return ("", 200)


# 2	Texture editing mode
@app.route("/mapper/texture_mode/", methods=["POST"])
def texture_mode():
    keyboard.write("2")
    info = "Texture Editing Mode"
    return ("", 200)


# 3	Projection mapping mode, use this to select a surface first
@app.route("/mapper/mapping_mode/", methods=["POST"])
def mapping_mode():
    keyboard.write("3")
    info = "Projection mapping mode"
    return ("", 200)


# 4	Source selection mode
@app.route("/mapper/source_selection_mode/", methods=["POST"])
def source_selection_mode():
    keyboard.write("4")
    info = "Source selection mode"
    return ("", 200)


# i	Show info Controls
@app.route("/mapper/show_controls/", methods=["POST"])
def show_controls():
    keyboard.write("i")
    info = "Show info Controls"
    return ("", 200)


# t	Add triangle surface
@app.route("/mapper/add_triangle/", methods=["POST"])
def add_triangle():
    keyboard.write("t")
    info = "Addeded Triangle"
    return ("", 200)


# q	Add quad surface
@app.route("/mapper/add_quad/", methods=["POST"])
def add_quad():
    keyboard.write("q")
    info = "Addeded Quad"
    return ("", 200)


# g	Add grid warp surface
@app.route("/mapper/add_grid/", methods=["POST"])
def add_grid():
    keyboard.write("g")
    info = "Addeded Grid Warp"
    return ("", 200)


# c	Add circle surface
@app.route("/mapper/add_circle/", methods=["POST"])
def add_circle():
    keyboard.write("c")
    info = "Add circle surface"
    return ("", 200)


# d	duplicate selected surface
@app.route("/mapper/duplicate/", methods=["POST"])
def duplicate():
    keyboard.write("d")
    info = "Duplicated Selected Surface"
    return ("", 200)


# +	Scale surface up
@app.route("/mapper/scale_up/", methods=["POST"])
def scale_up():
    keyboard.write("+")
    info = "Scaled surface up +"
    return ("", 200)


# -	Scale surface down
# NOT WORKING
@app.route("/mapper/scale_down/", methods=["POST"])
def scale_down():
    keyboard.write("-")
    info = "Scale surface down -"
    return ("", 200)

# TODO:add
# p	toggle perspective warping (quad surfaces only)
@app.route("/mapper/toggle_perspective/", methods=["POST"])
def toggle_perspective():
    keyboard.write("p")
    info = "Toggle perspective warping<br/>(quad surfaces only)"
    return ("", 200)


# ]	add columns to grid surface (grid warp surfaces only)
@app.route("/mapper/add_columns/", methods=["POST"])
def add_columns():
    keyboard.press_and_release("]")
    info = "add columns to grid surface<br/>(grid warp surfaces only)"
    return ("", 200)


# [	remove columns from grid surface (grid warp surfaces only)
@app.route("/mapper/remove_columns/", methods=["POST"])
def remove_columns():
    keyboard.press_and_release("[")
    info = "remove columns from grid surface<br/>(grid warp surfaces only)"
    return ("", 200)


# }	add rows to grid surface (grid warp surfaces only)
@app.route("/mapper/add_rows/", methods=["POST"])
def add_rows():
    keyboard.write("}")
    info = "add rows to grid surface<br/>(grid warp surfaces only)"
    return ("", 200)


# {	remove rows from grid surface (grid warp surfaces only)
@app.route("/mapper/remove_rows/", methods=["POST"])
def remove_rows():
    keyboard.write("{")
    info = "remove rows from grid surface<br/>(grid warp surfaces only)"
    return ("", 200)


# .	select next surface (projection mapping mode only)
@app.route("/mapper/next_surface/", methods=["POST"])
def next_surface():
    keyboard.write(".")
    info = "select next surface<br/>(projection mapping mode only)"
    return ("", 200)


# ,	select previous surface (projection mapping mode only)
@app.route("/mapper/previous_surface/", methods=["POST"])
def previous_surface():
    keyboard.write(",")
    info = "select previous surface<br/>(projection mapping mode only)"
    return ("", 200)


# >	select next vertex
@app.route("/mapper/next_vertex/", methods=["POST"])
def next_vertex():
    keyboard.write(">")
    info = "select next vertex<br/>(projection mapping mode only)"
    return ("", 200)


# <	select previous vertex
@app.route("/mapper/previous_vertex/", methods=["POST"])
def previous_vertex():
    keyboard.write("<")
    info = "previous next vertex<br/>(projection mapping mode only)"
    return ("", 200)


# 0	Move selected surface one layer up


@app.route("/mapper/layer_up/", methods=["POST"])
def layer_up():
    keyboard.write("0")
    info = "Move selected surface one layer up<br/>(projection mapping mode only)"
    return ("", 200)


# 9	Move selected surface one layer down


@app.route("/mapper/layer_down/", methods=["POST"])
def layer_down():
    keyboard.write("9")
    info = "Move selected surface one layer down<br/>(projection mapping mode only)"
    return ("", 200)


# s	Save composition
@app.route("/mapper/mapper_save/", methods=["POST"])
def save_mapper():
    keyboard.write("ss")
    info = "Saved"
    return ("", 200)


# l	Hide/show layer panel
@app.route("/mapper/layer_panel/", methods=["POST"])
def layer_panel():
    keyboard.write("l")
    info = "Hide/show layer panel"
    return ("", 200)


# z	Undo
@app.route("/mapper/Undo/", methods=["POST"])
def Undo():
    keyboard.write("z")
    info = "Undo"
    return ("", 200)


# new	Clear composition (remove all surfaces)
@app.route("/mapper/newcomp/", methods=["POST"])
def newcomp():
    keyboard.write("new")
    info = "Clear composition<br/>(remove all surfaces)"
    return ("", 200)


# BACKSPACE ('' via SSH)	Delete surface.
@app.route("/mapper/delete/", methods=["POST"])
def BACKSPACE():
    keyboard.send("backspace")
    info = "Delete surface"
    return ("", 200)


# SPACE	Toggle pause for video sources (texture and projection mapping modes)
@app.route("/mapper/pause/", methods=["POST"])
def SPACE():
    keyboard.send("space")
    info = "Pause"
    return ("", 200)


# TAB	Select next source (no need to use the source selection interface)
@app.route("/mapper/next_source/", methods=["POST"])
def next_source():
    keyboard.send("tab")
    info = "Select next source<br/>(no need to use the source selection interface)"
    return ("", 200)


# Arrow keys	Move selection. If no surface is selected in the projection mapping mode, all surfaces are moved.
@app.route("/mapper/arrow_up/", methods=["POST"])
def arrow_up():
    keyboard.send("up")
    info = "arrow up"
    return ("", 200)


@app.route("/mapper/arrow_down/", methods=["POST"])
def arrow_down():
    keyboard.send("down")
    info = "arrow down"
    return ("", 200)


@app.route("/mapper/arrow_left/", methods=["POST"])
def arrow_left():
    keyboard.send("left")
    info = "arrow left"
    return ("", 200)


@app.route("/mapper/arrow_right/", methods=["POST"])
def arrow_right():
    keyboard.send("right")
    info = "arrow right"
    return ("", 200)


# /	Toggle 1px/10px steps for keyboard moves on Raspberry Pi
@app.route("/mapper/accuracy/", methods=["POST"])
def accuracy():
    keyboard.send("/")
    info = "Toggle 1px/10px steps for keyboard moves on Raspberry Pi"
    return ("", 200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
    # app.run()
