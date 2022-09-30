


from types import NoneType


class Percept:
    northPercept = None
    westPercept = None
    eastPercept = None
    southPercept = None
       
    def setNorthPercept(self,northPercept):
        self.northPercept = northPercept
    def getNorthPercept(self):
        return  self.northPercept
    def setWestPercept(self,westPercept):
        self.westPercept = westPercept
    def getWestPercept(self):
        return self.westPercept
    def setEastPercept(self, eastPercept):
        self.eastPercept = eastPercept
    def getEastPercept(self):
        return self.eastPercept
    def setSouthPercept(self, southPercept):
        self.southPercept = southPercept
    def getSouthPercept(self):
        return self.southPercept
    def print(self):
        return f'northPercept: {self.northPercept} \n westPercept: {self.westPercept}\n eastPercept: {self.eastPercept} \n southPercept: {self.southPercept}'



        