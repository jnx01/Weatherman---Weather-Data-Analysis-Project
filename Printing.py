


from colorama import Fore

class PrintResult:

def printYearResult(self, values):

highestDate = values[0]
month_name = highestDate.strftime("%B")
print('\nHighest {0}C on {1} {2}'.format(values[1], month_name, highestDate.day))

lowestDate = values[2]
month_name = lowestDate.strftime("%B")
print('Lowest {0}C on {1} {2}'.format(values[3], month_name, lowestDate.day))

mostHumidDate = values[4]
month_name = mostHumidDate.strftime("%B")
print('Humidity {0}% on {1} {2}\n'.format(values[5], month_name, mostHumidDate.day))

def printMonthAvgs(self, avgs):
print('\nHighest Average: {0}C'.format(int(avgs[0])))
print('Lowest Average: {0}C'.format(int(avgs[1])))
print('Average Mean Humidity: {0}%\n\n'.format(int(avgs[2])))

def monthTemperatures(self, data):

month_name = data[0].date.strftime("%B")
print(month_name, data[0].date.year, '\n')

for i in range(len(data)):
if data[i].maxTemp != -100 and data[i].minTemp != 10000:
dayDate = data[i].date
highTemp = str(dayDate.day) + ' '
lowTemp = str(dayDate.day) + ' '
highTemp += str(''.join(['+' for j in range(data[i].maxTemp)]))
lowTemp += str(''.join(['+' for j in range(data[i].minTemp)]))
highTemp += ' ' + str(data[i].maxTemp) + 'C'
lowTemp += ' ' + str(data[i].minTemp) + 'C'
print(Fore.RED + highTemp)
print(Fore.BLUE + lowTemp, '\n')

def monthTempBarGraph(self,data):

month_name = data[0].date.strftime("%B")
print(month_name, data[0].date.year, '\n')

for i in range(len(data)):
if data[i].maxTemp != -100 and data[i].minTemp != 10000:
dayDate = data[i].date
tempRange = str(dayDate.day) + ' '
tempRange += str(''.join(['+' for j in range(data[i].minTemp)]))
lowCount = len(tempRange)
tempRange += str(''.join(['+' for j in range(data[i].maxTemp)]))
tempRange += ' {0}C - {1}C'.format(data[i].minTemp, data[i].maxTemp)
print(Fore.BLUE + tempRange[0:lowCount], Fore.RED + tempRange[lowCount:])
