class Device():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def getDescription(self):
        return self.description

    def getName(self):
        return self.name
