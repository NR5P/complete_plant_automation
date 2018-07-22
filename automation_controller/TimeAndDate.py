import datetime


def showCurrentTimeDate():
    print("The current date and time is {}".format(datetime.datetime.now()))

def changeDate():
    # https://www.cyberciti.biz/faq/howto-set-date-time-from-linux-command-prompt/
    # https://docs.python.org/3/library/os.html
    # for changing date and time with os.system
    currentDisplay = "day"
    showCurrentTimeDate()
    answer = input("would you like to change it? enter y or n ")
    try:
        if answer == "y":
            newDateTime = input("please enter date and time with format ex: 2 OCT 2006 18:00:00\nthen press enter ")
            os.system("date -s " + newDateTime)
    except:
        print("please enter date/time in correct format")

            
            
