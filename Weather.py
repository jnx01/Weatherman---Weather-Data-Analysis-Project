

from datetime import datetime

class WeatherData:

def __init__(self, row):

self.date = datetime.strptime(row[0], '%Y-%m-%d').date()
self.maxTemp = self.fillValue(row[1], 0)
self.meanTemp = self.fillValue(row[2], 0)
self.minTemp = self.fillValue(row[3], 1)
self.maxHumid = self.fillValue(row[7], 0)
self.meanHumid = self.fillValue(row[8], 0)
self.minHumid = self.fillValue(row[9], 0)

def fillValue(self,value, minTempCheck):
if value != '' and value != '\n':
return int(float(value))
else:
if minTempCheck == 0:
return -100
else:
return 10000
