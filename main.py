from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import numpy as np
import datetime
global calLayout,row
from calendar import monthrange
currentTime=datetime.datetime.now()
curYear=currentTime.year
curMonth=currentTime.month
class Calendar(GridLayout):
    def __init__(self, **kwargs):
        global calendarRow,calLayout
        calendarRow=[]
        super(Calendar, self).__init__(**kwargs)
        def createYear(Y,M):
            firstDay=datetime.datetime(Y,M,1)
            print(firstDay.strftime("%Y %b %w"))
            print(monthrange(Y,M)[1])
            firstWeekday=firstDay.strftime("%w")
            if firstWeekday != 1:
                for i in range(int(firstWeekday)-1):
                    calendarRow.append("")
            else:
                print("Month starts on Monday")
            for i in range(monthrange(Y,M)[1]):
                calendarRow.append(i+1)
            if len(calendarRow)<35:
                for i in range (35-len(calendarRow)):
                    calendarRow.append("")
            print(calendarRow)
        createYear(curYear,curMonth)
        calendarRow=np.array(calendarRow)
        calLayout=calendarRow.reshape(5,7)
        print(calLayout)
        for row in calLayout:
            for label in row:
                calElem=Button(text=label)
                calElem.bind(on_press=self.on_button_press)
class MyApp(App):
    def build(self):
        return Calendar()
if __name__ == "__main__":
    MyApp().run()




