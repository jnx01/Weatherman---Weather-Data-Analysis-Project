


from datetime import datetime
from csv import reader
from Weather import WeatherData

class ReadDataFromFile:

def findFileAndRead(self, basepath, year, month=''):
self.data = []
path = str(basepath)
if month == '':
for i in range(1, 13):
datetime_object = datetime.strptime(str(i), "%m")
month_name = datetime_object.strftime("%b")
filepath = path + '/Murree_weather_' + str(year) + '_' + month_name + '.txt'
self.openFile(filepath, month)
else:
filepath = path + '/Murree_weather_' + str(year) + '_' + month + '.txt'
self.openFile(filepath, month)

def openFile(self, path, month):
month_i_data = []
try:
with open(path, 'r') as csv_file:
csv_reader = reader(csv_file, delimiter=',')
for row in csv_reader:
if row[0] != 'PKT' and row[0] != 'PKST':
day = WeatherData(row)
month_i_data.append(day)
if month == '':
self.data.append(month_i_data)
else:
self.data = month_i_data
csv_file.close()
except FileNotFoundError:
if month == '':
self.data.append([])
else:
print("Requested month data doesn't exist")
exit()
