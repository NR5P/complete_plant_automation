from TimeAndDate import showCurrentTimeDate, changeDate
from irrigationTimer import Valve
from timer_socket import *
import sys
import pickle
import re
import datetime
import socket



def displayMainMenu(conn):
    conn.send(str.encode("""
Main menu  

1. show valves currently running
2. list valves on
3. list valve times
4. view all valve settings
5. edit valve     
6. show time 
7. change time and date
    """))

def mainMenu(conn):
    while True:
        displayMainMenu(conn)
        conn.send(str.encode("\nenter: "))
        mainMenuInput = int(conn.recv(1024).decode("utf-8"))
        if mainMenuInput == 1:
            showValvesRunning(conn)
        elif mainMenuInput == 2:
            showValvesOn(conn)
        elif mainMenuInput == 3:
            showValveTimes(conn)
        elif mainMenuInput == 4:
            displayAllSettings(conn)
        elif mainMenuInput == 5:
            mainMenuEditValve(conn)
        elif mainMenuInput == 6:
            showCurrentTimeDate()
        elif mainMenuInput == 7:
            changeDate()
        else:
            conn.send(str.encode("please enter a valid input!!!"))

def displayAllSettings(conn):
    vNumber = 0
    for i in Valve.valveList:
        vNumber += 1
        conn.send(str.encode("valve {}".center(30, "=").format(vNumber)))
        print("")
        conn.send(str.encode("\non/off: {}\n".format(i.onOff)))
        conn.send(str.encode("connected to pin {}\n".format(i.pin)))
        conn.send(str.encode("is it currently running on or off: {}\n".format(i.currentState)))
        if len(i.days) == 0:
            conn.send(str.encode("days on: no days selected\n"))
        else:
            conn.send(str.encode("days on: {}\n".format(i.days)))
        if len(i.irrigationTime) > 0:
            conn.send(str.encode("irrigation times: \n"))
            listTimesAndDurations(i)
        else:
            conn.send(str.encode("irrigation times: there are no irrigation times set\n"))
        if i.cycleOnTime:
            conn.send(str.encode("cycle on time: {}: \n".format(deltaToMinSec(i.cycleOnTime))))
        else:
            conn.send(str.encode("no cycle on time set yet\n"))
        if i.cycleOffTime:
            conn.send(str.encode("cycle off time: {}\n".format(deltaToHrMinSec(i.cycleOffTime))))
        else:
            conn.send(str.encode("no cycle off time set yet\n"))
        if i.blackoutStart:
            conn.send(str.encode("blackout start time: {}\n".format(i.blackoutStart.strftime("%H:%M:%S"))))
        else:
            conn.send(str.encode("no blackout start time set yet\n"))
        if i.blackoutStop:
            conn.send(str.encode("blackout stop time: {}\n\n".format(i.blackoutStop.strftime("%H:%M:%S"))))
        else:
            conn.send(str.encode("no blackout stop time set yet\n"))
    mainMenu(conn)

def mainMenuEditValve(conn):
    conn.send(str.encode("enter valve to edit ex: 1, 2, 3 etc."))
    valveAnswer = int(conn.recv(1024).decode("utf-8"))-1
    valveAnswer = Valve.valveList[valveAnswer]
    conn.send(str.encode("to edit on/off=onoff"))
    conn.send(str.encode("to edit days on=days"))
    conn.send(str.encode("to edit irrigation times=times"))
    conn.send(str.encode("to edit irrigation time durations=duration"))
    conn.send(str.encode("to edit cycle on time=cycle on"))
    conn.send(str.encode("to edit cycle off time=cycle off"))
    conn.send(str.encode("to edit blackout start time=blackout start"))
    conn.send(str.encode("to edit blackout stop time=blackout stop\n"))
    conn.send(str.encode("""
1. turn on/off
2. change days on
3. irrigation times
4. irrigation time duration
5. cycle on time
6. cycle off time
7. blackout start time
8. blackout stop time   
9. reset valve settings 
10. cycle or irrigate
11. back to main menu
    """))
    conn.send(str.encode("enter: "))
    answer = int(conn.recv(1024).decode("utf-8"))
    if answer == 1:
        setOnOff(conn, valveAnswer)
    elif answer == 2:
        setDays(conn, valveAnswer)
    elif answer == 3:
        setTimes(conn, valveAnswer)
    elif answer == 4:
        setDuration(conn, valveAnswer)
    elif answer == 5:
        setCycleOn(conn, valveAnswer)
    elif answer == 6:
        setCycleOff(conn, valveAnswer)
    elif answer == 7:
        setBlackoutStart(conn, valveAnswer)
    elif answer == 8:
        setBlackoutStop(conn, valveAnswer)
    elif answer == 9:
        resetValve(conn, valveAnswer)
    elif answer == 10:
        cycleOrIrrigate(conn, valveAnswer)
    elif answer == 11:
        mainMenu()
    else:
        conn.send(str.encode("enter valid input"))

def setOnOff(conn, valveAnswer):
    conn.send(str.encode("{} is currently {}".format(valveAnswer, valveAnswer.onOff)))
    conn.send(str.encode("enter on or off and press enter"))
    onOffAnswer = conn.recv(1024).decode("utf-8")
    if onOffAnswer == "off":
        valveAnswer.onOff = "off"
        conn.send(str.encode("{} is currently {}".format(valveAnswer, valveAnswer.onOff)))
        valveAnswer.saveValve()
    elif onOffAnswer =="on":
        valveAnswer.onOff = "on"
        conn.send(str.encode("{} is currently {}".format(valveAnswer, valveAnswer.onOff)))
        valveAnswer.saveValve()
    else:
        conn.send(str.encode("enter valid input"))

def setDays(conn, valveAnswer):
    dayRegex = re.compile(r"monday|tuesday|wednesday|thursday|friday|saturday|sunday")
    addOrDeleteRegex = re.compile(r"add|delete")
    if len(valveAnswer.days) != 0:
        conn.send(str.encode(("{} is currently set to run on {}").format(valveAnswer, valveAnswer.days)))
    else:
        conn.send(str.encode("{} currently has no days set".format(valveAnswer)))
    conn.send(str.encode("please type 'add' or 'delete': "))
    addDeleteAnswer = conn.recv(1024).decode("utf-8")
    regexAnswer = addOrDeleteRegex.search(addDeleteAnswer)
    conn.send(str.encode("Please enter days to {}: ".format(regexAnswer.group())))
    daysAnswer = conn.recv(1024).decode("utf-8")
    regexDays = dayRegex.findall(daysAnswer)
    if regexAnswer.group() == "add":
        for i in regexDays: valveAnswer.days.add(i.title())
        valveAnswer.saveValve()
        if len(valveAnswer.days) != 0:
            conn.send(str.encode("{} is currently set to run on {}: ".format(valveAnswer, valveAnswer.days)))
        else:
            conn.send(str.encode("{} currently has no days set".format(valveAnswer)))
    elif regexAnswer.group() == "delete":
        for i in regexDays: valveAnswer.days.remove(i.title())
        valveAnswer.saveValve()
        conn.send(str.encode("{} is currently set to run on {}: ".format(valveAnswer, valveAnswer.days)))
    else:
        conn.send(str.encode("enter correct format"))


def setTimes(conn, valveAnswer):
    regex = re.compile(r"(add|delete) (\d\d:\d\d)")
    conn.send(str.encode("current irrigation times"))
    listTimesAndDurations(valveAnswer)
    conn.send(str.encode("to add or delete times type in exact format ex. add 18:00: "))
    answer = conn.recv(1024).decode("utf-8")
    mo = regex.search(answer)
    time = makeTimeFromDateTime(mo.group(2))
    if mo.group(1) == "add":
        valveAnswer.irrigationTime[time] = None
        valveAnswer.saveValve()
        conn.send(str.encode("\ncurrent irrigation times:\n"))
        listTimesAndDurations(valveAnswer)
        setDuration(valveAnswer, time)
    elif mo.group(1) == "delete":
        del valveAnswer.irrigationTime[time]
        valveAnswer.saveValve()
        listTimesAndDurations(valveAnswer)
    else:
        conn.send(str.encode("please enter correct format"))

def makeTimeFromDateTime(theRegexTimePart):
    splitted = theRegexTimePart.split(":")
    hour = int(splitted[0])
    minute = int(splitted[1])
    return datetime.time(hour = hour, minute = minute)

def listTimesAndDurations(conn, valveAnswer):
        for key, value in valveAnswer.irrigationTime.items():
            conn.send(str.encode("time: " + key.strftime("%H:%M")))
            if value != None:
                conn.send(str.encode("duration: {}\n".format(deltaToHrMinSec(value))))
            else:
                conn.send(str.encode("None"))

def setDuration(conn, valveAnswer, timeFromSetTimes=None):
    if timeFromSetTimes:
        time = timeFromSetTimes
        valveAnswer.saveValve()
    else:
        listTimesAndDurations(valveAnswer)
        conn.send(str.encode("\n\nenter time to modify"))
        timeInput = conn.recv(1024).decode("utf-8")
        time = datetime.datetime.strptime(timeInput, "%H:%M")
    conn.send(str.encode("\nenter the duration in hours and minutes, ex. 00:30 or 2:30: "))
    duration = conn.recv(1024).decode("utf-8")
    strippedDuration = datetime.datetime.strptime(duration, "%H:%M")
    durationDelta = datetime.timedelta(hours = strippedDuration.hour, minutes = strippedDuration.minute, seconds = strippedDuration.second)
    valveAnswer.irrigationTime[time] = durationDelta
    valveAnswer.saveValve()
    listTimesAndDurations(valveAnswer)

def setCycleOn(conn, valveAnswer):
    if valveAnswer.cycleOnTime != None:
        #minutes = valveAnswer.cycleOnTime.seconds / 60
        #seconds = valveAnswer.cycleOnTime.seconds % 60
        conn.send(str.encode("cycle on time is currently: {}".format(deltaToMinSec(valveAnswer.cycleOnTime))))
    else:
        conn.send(str.encode("no cycle on time set yet"))
    conn.send(str.encode("type new time in format minutes:seconds ex. 18:30 here: "))
    answer = conn.recv(1024).decode("utf-8")
    answerStripped = datetime.datetime.strptime(answer, "%M:%S")
    valveAnswer.cycleOnTime = datetime.timedelta(minutes = answerStripped.minute, seconds = answerStripped.second)
    valveAnswer.saveValve()
    #minutes = valveAnswer.cycleOnTime.seconds / 60
    #seconds = valveAnswer.cycleOnTime.seconds % 60
    conn.send(str.encode("cycle on time is currently: {}".format(deltaToMinSec(valveAnswer.cycleOnTime))))

def setCycleOff(conn, valveAnswer):
    if valveAnswer.cycleOffTime != None:
        conn.send(str.encode("cycle off time is currently: {}".format(deltaToHrMinSec(valveAnswer.cycleOffTime))))
    else:
        conn.send(str.encode("no cycle off time set yet"))
    conn.send(str.encode("type new time in format hours:minutes:seconds ex. 18:30:00 here: "))
    answer = conn.recv(1024).decode("utf-8")
    answerStripped = datetime.datetime.strptime(answer, "%H:%M:%S")
    valveAnswer.cycleOffTime = datetime.timedelta(hours = answerStripped.hour, minutes = answerStripped.minute, seconds = answerStripped.second)
    valveAnswer.saveValve()
    #minutes = valveAnswer.cycleOffTime.seconds / 60
    #seconds = valveAnswer.cycleOffTime.seconds % 60
    conn.send(str.encode("cycle off time is currently: {}".format(deltaToHrMinSec(valveAnswer.cycleOffTime))))

def setBlackoutStart(conn,valveAnswer):
    conn.send(str.encode("current blackout start is: {}".format(valveAnswer.blackoutStart.strftime("%H:%M:%S"))))
    conn.send(str.encode("enter start time with format 18:30:00: "))
    answer = conn.recv(1024).decode("utf-8")
    strippedAnswer = datetime.datetime.strptime(answer, "%H:%M:%S")
    valveAnswer.blackoutStart = strippedAnswer
    valveAnswer.saveValve()
    conn.send(str.encode("current blackout start is: {}".format(valveAnswer.blackoutStart.strftime("%H:%M:%S"))))

def setBlackoutStop(conn, valveAnswer):
    conn.send(str.encode("current blackout stop is: {}".format(valveAnswer.blackoutStop.strftime("%H:%M:%S"))))
    conn.send(str.encode("enter stop time with format 18:30:00: "))
    answer = conn.recv(1024).decode("utf-8")
    strippedAnswer = datetime.datetime.strptime(answer, "%H:%M:%S")
    valveAnswer.saveValve()
    valveAnswer.blackoutStop = strippedAnswer
    conn.send(str.encode("current blackout stop is: {}".format(valveAnswer.blackoutStop.strftime("%H:%M:%S"))))

def resetValve(conn, valveAnswer):
    conn.send(str.encode("""
    *************************************
    are you sure you want to reset valve?

    enter yes or no
    *************************************

        """))
    conn.send(str.encode("enter: "))
    answer = conn.recv(1024).decode("utf-8")
    if answer == "yes":
        valveAnswer.onOff = "off"
        valveAnswer.cycleOrIrrigate = None
        valveAnswer.currentState = "off"
        valveAnswer.irrigationTime = {}
        valveAnswer.cycleOnTime = None
        valveAnswer.cycleOffTime = None
        valveAnswer.blackoutStart = None
        valveAnswer.blackoutStop = None
        valveAnswer.days = set()
        valveAnswer.saveValve()
    elif answer == "no":
        mainMenu()
    else:
        conn.send(str.encode("invalid input"))

def cycleOrIrrigate(conn, valveAnswer):
    conn.send(str.encode("{} is currently set on {}".format(valveAnswer, valveAnswer.cycleOrIrrigate)))
    conn.send(str.encode("""
please enter:
    1. cycle
    2. irrigate
    3. main menu
    """))
    answer = int(conn.recv(1024).decode("utf-8"))
    if answer == 1:
        valveAnswer.cycleOrIrrigate = "cycle"
        valveAnswer.saveValve()
        conn.send(str.encode("{} is set to cycle".format(valveAnswer)))
    elif answer == 2:
        valveAnswer.cycleOrIrrigate = "irrigate"
        valveAnswer.saveValve()
        conn.send(str.encode("{} is set to irrigate".format(valveAnswer)))
    elif answer == 3:
        mainMenu()
    else:
        conn.send(str.encode("invalid input"))

def showValvesRunning(conn):
    for i in Valve.valveList:
        if i.currentState == "on":
            conn.send(str.encode("\t {} is running".format(i)))
    if i.currentState == "off":
        conn.send(str.encode("no valves are currently running"))

def showValvesOn(conn):
    lsNumber = 0
    for i in Valve.valveList:
        lsNumber += 1
        if i.onOff == "on":
            conn.send(str.encode("valve {} is on".format(lsNumber)))
        elif i.onOff == "off":
            conn.send(str.encode("valve {} is off".format(lsNumber)))

def showValveTimes(conn):
    vNumber = 0
    for i in Valve.valveList:
        for key, value in i.irrigationTime.items():
            vNumber += 1
            conn.send(str.encode("valve {}".format(vNumber)))
            conn.send(str.encode("time: " + key.strftime("%H:%M")))
            conn.send(str.encode("duration: \n\n" + value.strftime("%H:%M:%S")))
    if vNumber == 0:
        conn.send(str.encode("there are no irrigation times set"))

def deltaToMinSec(delta):
    seconds = delta.seconds
    minutes = seconds // 60
    seconds = seconds - (minutes * 60)
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    return "{}:{}".format(minutes, seconds)


def deltaToHrMinSec(delta):
    seconds = delta.seconds
    hours = seconds // 3600
    seconds = seconds - (hours * 3600)
    minutes = seconds // 60
    seconds = seconds - (minutes * 60)
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    if len(str(hours)) < 2:
        hours = "0" + str(hours)
    return "{}:{}:{}".format(hours, minutes, seconds)

def deltaToHrMin(delta):
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = seconds // 60
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    if len(str(hours)) < 2:
        hours = "0" + str(hours)

def turn_off():
    GPIO.output(valve1Pin, False)
    GPIO.output(valve2Pin, False)
    GPIO.output(valve3Pin, False)
    GPIO.output(valve4Pin, False)
    GPIO.output(valve5Pin, False)
    GPIO.output(valve6Pin, False)
    GPIO.output(valve7Pin, False)
    GPIO.output(valve8Pin, False)
    GPIO.output(valve9Pin, False)
    GPIO.output(valve10Pin, False)
    os.system("poweroff now")

def restart():
    GPIO.output(valve1Pin, False)
    GPIO.output(valve2Pin, False)
    GPIO.output(valve3Pin, False)
    GPIO.output(valve4Pin, False)
    GPIO.output(valve5Pin, False)
    GPIO.output(valve6Pin, False)
    GPIO.output(valve7Pin, False)
    GPIO.output(valve8Pin, False)
    GPIO.output(valve9Pin, False)
    GPIO.output(valve10Pin, False)
    os.system("reboot")



































