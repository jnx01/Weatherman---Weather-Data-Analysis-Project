


from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from CalculateAndPrint import CallCalculateAndPrint
from ReadData import ReadDataFromFile

def validDateFor_e(e):
if e is not None:
arg_year = datetime.strptime(e, '%Y')
return arg_year

def validDateFor_a_or_c(a_or_c):
if a_or_c is not None:
arg_year_month = datetime.strptime(a_or_c, '%Y/%m')
return arg_year_month

parser = ArgumentParser()
parser.add_argument('file_path', type=Path)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', type=validDateFor_e)
group.add_argument('-c', type=validDateFor_a_or_c)
group.add_argument('-a', type=validDateFor_a_or_c)
args = parser.parse_args()
basepath = args.file_path

if basepath.exists():
if args.e is not None:
year_data = ReadDataFromFile()
year_data.findFileAndRead(basepath, args.e.year)
results = CallCalculateAndPrint()
results.yearResults(year_data.data)

elif args.c is not None or args.a is not None:
if args.c is not None:
year_month = args.c
else:
year_month = args.a
year_month_data = ReadDataFromFile()
year_month_data.findFileAndRead(basepath, year_month.year, year_month.strftime("%b"))
results = CallCalculateAndPrint()
results.monthResults(year_month_data.data)

else:
print('\nSomething wrong with the arguments\n')
