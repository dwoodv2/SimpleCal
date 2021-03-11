import datetime

import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

global calLayout,row
from calendar import monthrange
currentTime=datetime.datetime.now()
curYear=currentTime.year
curMonth=currentTime.month
class MyApp(App):
    def build(self):
        global calendarRow,calLayout
        calendarRow=[]
        main_layout=BoxLayout(orientation="vertical")
        self.date=Label(text=str(currentTime))
        main_layout.add_widget(self.date)
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
        calGrid = GridLayout(rows=5, cols=7)
        for row in calLayout:
            for label in row:
                print(label)
                calElem=Button(text=label)
                calElem.bind()
                calGrid.add_widget(calElem)
        main_layout.add_widget(calGrid)
        return main_layout#Return after all widgets are added
    def on_elem_press(self,instance):
        print("test")
if __name__ == "__main__":
    app=MyApp()
    app.run()




