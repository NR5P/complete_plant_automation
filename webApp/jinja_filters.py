import time

def deltaToHrMin(delta):
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = seconds // 60
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    if len(str(hours)) < 2:
        hours = "0" + str(hours)

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

def strf_time_converter(time):
    return time.strftime("%H:%M")

def trueFalseIndication(i):
    if i:
        return "on"
    else:
        return "off"