
from Calculations import Calculate
from Printing import PrintResult

class CallCalculateAndPrint:

def yearResults(self, data):
calculatedResult = Calculate()
calculatedResult.yearStats(data)
printResult = PrintResult()
printResult.printYearResult(calculatedResult.values)

def monthResults(self, data):
calculatedResult = Calculate()
calculatedResult.monthStats(data)
printResult = PrintResult()
printResult.printMonthAvgs(calculatedResult.avgs)
printResult.monthTemperatures(data)
printResult.monthTempBarGraph(data)
