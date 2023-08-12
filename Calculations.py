

class Calculate:

def yearStats(self, data):

highestTemps = []
lowestTemps = []
mostHumidDays = []

for i in data:
if len(i) != 0:
index = i.index(max(i, key=lambda x: x.maxTemp))
highestTemps.append([i[index].date, i[index].maxTemp])
index = i.index(min(i, key=lambda x: x.minTemp))
lowestTemps.append([i[index].date, i[index].minTemp])
index = i.index(max(i, key=lambda x: x.maxHumid))
mostHumidDays.append([i[index].date, i[index].maxHumid])

highest = max(highestTemps, key=lambda x: x[1])
lowest = min(lowestTemps, key=lambda x: x[1])
mostHumid = max(mostHumidDays, key=lambda x: x[1])
self.values = highest + lowest + mostHumid

def monthStats(self, data):
high = 0
low = 0
meanHumid = 0
count = [0, 0, 0]

if len(data) != 0:

high = sum(i.maxTemp for i in data if i.maxTemp != -100)
low = sum(i.minTemp for i in data if i.minTemp != 10000)
meanHumid = sum(i.meanHumid for i in data if i.meanHumid != -100)
count[0] = sum(1 for i in data if i.maxTemp != -100)
count[1] = sum(1 for i in data if i.minTemp != 10000)
count[2] = sum(1 for i in data if i.meanHumid != -100)

findAvg = lambda: [high/count[0], low/count[1], meanHumid/count[2]]
self.avgs = findAvg()
