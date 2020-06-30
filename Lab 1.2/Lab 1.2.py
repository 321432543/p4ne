from matplotlib import pyplot
from openpyxl import load_workbook as wb

a = wb('data_analysis_lab.xlsx')
spisok = a['Data']   # присваиваем списку значения вкладки Data из xlsx


spisok['A'][1:]
spisok['C'][1:]
spisok['D'][1:]

def getvalue(x): return x.value


year = list(map(getvalue, spisok['A'][1:]))
temp = list(map(getvalue, spisok['C'][1:]))
act = list(map(getvalue, spisok['D'][1:]))

pyplot.plot(year, temp, label="Температура")
pyplot.plot(year, act, label="Активность")

pyplot.show()