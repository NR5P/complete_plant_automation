"""
base class for each automation component. 
"""

import pickle

class Timer():
    timer_list = []
    count = None # number of components currently running

    def __init__(self, pin, notes, name = f"component {count}", on = False, test = False, currentStateOn = False):
        self.name = name
        self.pin = pin
        self.on = on
        self.currentlyOn = False # this is if the component is running in real time or not
        self.test = test
        self.currentStateOn = currentStateOn
        self.notes = notes
        self.save()

    def __str__(self):
        return self.name


    def save(self):
        f = open(self.name, "wb")
        pickle.dump(self, f)
        f.close()

    def load(self):
        f = open(self.name, "rb")
        self = pickle.load(f)
        f.close()

    @staticmethod
    def run():
        while True:
            for i in Timer.timer_list:
                i.run()
