from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import datetime
from calendar import monthrange
currentTime=datetime.datetime.now()
curYear=currentTime.year
curMonth=currentTime.month
def createYear(curYear,curMonth):
    firstDay=datetime.datetime(curYear,curMonth,1)
    print(firstDay.strftime("%Y %b %w"))
    print(monthrange(curYear,curMonth)[1])
    calendarRow=[]
    firstWeekday=firstDay.strftime("%w")
    if firstWeekday != 1:
        for i in range(int(firstWeekday)-1):
            calendarRow.append("")
    else:
        print("Month starts on Monday")
    for i in range(monthrange(curYear, curMonth)[1]):
        calendarRow.append(i+1)
    print(calendarRow)
createYear(2021,3)




