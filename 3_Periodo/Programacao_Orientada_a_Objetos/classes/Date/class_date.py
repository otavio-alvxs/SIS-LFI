def getDay(self):
    return self.day

def getMonth(self):
    return self.month

def getYear(self):
    return self.year

def setDay(self, newDay):
    self.__day = newDay

def setMonth(self, newMonth):
    self.__month = newMonth

def setYear(self, newYear):
    self.__year = newYear

def formatDate(self):
    print (f'{self.getYear()}/{self.getMonth()}/{self.getDay()}')