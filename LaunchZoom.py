#!usr/bin/python3

from os import system
from time import ctime
def getMeeting(link):
    system('open '+link)

now = ctime()
day = now[:3]
hour = int(now[11:13])
minute = int(now[14:16])
timevalue = (hour*60)+minute
classlist = []

class NSAclass(object):
    def __init__(self, classDays, classTimevalues, classLink):
        self.days = classDays
        self.timevalues = classTimevalues
        self.link = classLink
        classlist.append(self)

    def getZoomLink(self):
        print(len(self.days))
        for i in range(len(self.days)):
            print(self.days[i])
            print(self.timevalues[i])
            if day == self.days[i] and abs(timevalue - self.timevalues[i]) <= 15:
                getMeeting(self.link)
                raise Exception()
        return None

#"time values" are the number of minutes into the day a class is (out 1440 minutes in a day)
#Data Model
#classname = NSAclass([class days as 3 letter strings],[class time values as integers], 'zoom link as string')
#Data Template:
# = NSAclass([],[],'')
Greek = NSAclass(['Mon','Wed','Fri'],[660,660,600],'https://zoom.us/j/224236465?pwd=T1NibXZubFRCcVV4MmlqTXBGaUw0Zz09')



for i in classlist:
    try:
        i.getZoomLink()
    except:
        break

