class Device():
    def __init__(self, id, name, description, pin, onoff):
        self.id = id
        self.name = name
        self.description = description
        self.pin = pin
        self.onoff = onoff

    def getDescription(self):
        return self.description

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin

    def getOnoff(self):
        return self.onoff

    def setPin(self, pin):
        self.pin = pin

    def setOnOff(self, onoff):
        self.onoff = onoff