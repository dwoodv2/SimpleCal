import datetime

import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

global calLayout, row,calElem
from calendar import monthrange

currentTime = datetime.datetime.now()
curYear = currentTime.year
curMonth = currentTime.month
class MyApp(App):
    def build(self):
        year=str(currentTime.strftime("%Y"))
        month=str(currentTime.strftime("%B"))
        global calendarRow, calLayout
        calendarRow = []
        main_layout = BoxLayout(orientation="vertical")
        self.date = Label(text="Current Date : {0}".format(str(currentTime.strftime("%A %d %B %Y"))))
        self.selectedMonth = Label(text="{0} {1}".format(month,year))
        main_layout.add_widget(self.date)
        main_layout.add_widget(self.selectedMonth)
        def createYear(Y, M):
            firstDay = datetime.datetime(Y, M, 1)
            print(firstDay.strftime("%Y %b %w"))
            print(monthrange(Y, M)[1])
            firstWeekday = firstDay.strftime("%w")
            if firstWeekday != 1:
                for i in range(int(firstWeekday) - 1):
                    calendarRow.append("")
            else:
                print("Month starts on Monday")
            for i in range(monthrange(Y, M)[1]):
                calendarRow.append(i + 1)
            if len(calendarRow) < 35:
                for i in range(35 - len(calendarRow)):
                    calendarRow.append("")
            print(calendarRow)
        createYear(curYear, curMonth)  # 1st time opening program it will get the current date
        calendarRow = np.array(calendarRow)
        calLayout = calendarRow.reshape(5, 7)
        print(calLayout)
        calGrid = GridLayout(rows=6, cols=7)
        mLabel = Label(text="[i]Mon[/i]", markup=True)
        tLabel = Label(text="[i]Tue[/i]", markup=True)
        wLabel = Label(text="[i]Wed[/i]", markup=True)
        thLabel = Label(text="[i]Thu[/i]", markup=True)
        fLabel = Label(text="[i]Fri[/i]", markup=True)
        sLabel = Label(text="[i]Sat[/i]", markup=True)
        suLabel = Label(text="[i]Sun[/i]", markup=True)
        calGrid.add_widget(mLabel)
        calGrid.add_widget(tLabel)
        calGrid.add_widget(wLabel)
        calGrid.add_widget(thLabel)  # There must be a better way of doing this...
        calGrid.add_widget(fLabel)
        calGrid.add_widget(sLabel)
        calGrid.add_widget(suLabel)
        for row in calLayout:
            for label in row:
                if label == str(currentTime.strftime("%d")) and year==str(currentTime.strftime("%Y")) and month ==str(currentTime.strftime("%B")):
                    self.calElem = Button(text="[b][color=fc0303]{0}[/color][/b]".format(label),markup=True)
                    self.calElem.bind(on_press=self.on_elem_press)
                    calGrid.add_widget(self.calElem)
                    print("Today!")
                else:
                    print(label)
                    self.calElem = Button(text=label)
                    self.calElem.bind(on_press=self.on_elem_press)
                    calGrid.add_widget(self.calElem)
                    print(self.calElem.text)
        main_layout.add_widget(calGrid)
        return main_layout  # Return after all widgets are added
    def on_elem_press(self, instance):
        daySelected=instance.text
        print(daySelected)


if __name__ == "__main__":
    app = MyApp()
    app.run()
