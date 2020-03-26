#!/usr/local/bin/python3

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
    def __init__(self, classDays, classTimevalues, classLinks):
        self.days = classDays
        self.timevalues = classTimevalues
        self.links = classLinks
        classlist.append(self)
    def getZoomLink(self):
        for i in range(len(self.days)):
            if len(self.links) == 1:
                linkSelector = 0
            else:
                linkSelector = i
            if day == self.days[i] and abs(timevalue - self.timevalues[i]) <= 15:
                getMeeting(self.links[linkSelector])
                raise Exception()
        return None

#"time values" are the number of minutes into the day a class is (out 1440 minutes in a day)
#Data Model
#classname = NSAclass([class days as 3 letter strings],[class time values as integers], [zoom links as strings])
#Data Template:
# = NSAclass([],[],[])
# = only 1 link needed if all links are the same
Greek = NSAclass(['Mon','Wed','Fri'],[660,870,600], ['https://zoom.us/j/224236465?pwd=T1NibXZubFRCcVV4MmlqTXBGaUw0Zz09'])
Math = NSAclass(['Wed','Fri'],[930,720],['https://zoom.us/j/884206080?pwd=ZTdqcFVqUnpLZFh5bHFCRjZKNE9mdz09'])
Herpetology = NSAclass(['Mon','Thu'],[930,930],['https://zoom.us/j/586342576?pwd=STZZdE5ZNTdPOUxDZjJsa2t0WEpkQT09', 'https://zoom.us/j/442920669?pwd=dFJDSjl2eW1jSFlsS1dWQkh2WXd5UT09'])
PolEcon = NSAclass(['Mon','Wed','Thu'],[540,660,750],['https://zoom.us/j/6914342415'])
Choir = NSAclass(['Mon','Wed','Fri'],[780,780,840],['https://zoom.us/j/442302046?pwd=NjdoWjVNb09SNkdjSmdpMDBSeHlpZz09','https://zoom.us/j/596281397?pwd=cG5zSGFEdHZqMTlaTXo5QUxhZ0t6UT09','https://zoom.us/j/437828022?pwd=eCttUk5UcWQ0cXFaWFlPR1BpUXJoZz09'])
CompAndArrange = NSAclass(['Tue','Wed'],[780,540],['https://zoom.us/j/7442571164'])

for i in classlist:
    try:
        i.getZoomLink()
    except:
        break

