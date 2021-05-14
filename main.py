import datetime
import numpy as np
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

global calLayout, row, calElem, year, month, currentTime, createMonth, monthList, selmonth_label
from calendar import monthrange

currentTime = datetime.datetime.now()
curYear = currentTime.year
curMonth = currentTime.month
year = int(currentTime.strftime("%Y"))
month = int(currentTime.strftime("%m"))
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]


def on_elem_press(instance):
    daySelected = instance.text
    print(daySelected)


class MyApp(App):
    def build(self):
        global createMonth, calendarRow, main_layout, calGrid, build_calGrid
        calendarRow = []
        main_layout = BoxLayout(orientation="vertical", spacing=5)
        self.date = Label(text="Current Date : {0}".format(str(currentTime.strftime("%A %d %B %Y")), font_size='20sp'))
        self.selectedMonth = Label(text="{0} {1}".format(monthList[month - 1], year), font_size='20sp')
        button_layout = BoxLayout(orientation="horizontal")
        self.leftButton = Button(text="<", size_hint=(.2, .25), pos_hint={'x': .2, 'y': .2})
        self.rightButton = Button(text=">", size_hint=(.2, .25), pos_hint={'x': .3, 'y': .2})
        main_layout.add_widget(self.date)
        main_layout.add_widget(self.selectedMonth)
        self.leftButton.bind(on_press=self.left_button_pressed)
        self.rightButton.bind(on_press=self.right_button_pressed)
        button_layout.add_widget(self.leftButton)
        button_layout.add_widget(self.rightButton)
        main_layout.add_widget(button_layout)

        def createMonth(Y, M):
            global calLayout
            calendarRow = []
            firstDay = datetime.datetime(Y, M, 1)
            firstWeekday = firstDay.strftime("%w")
            if firstWeekday != 1:
                for i in range(int(firstWeekday) - 1):
                    calendarRow.append("")
            else:
                print("Month starts on Monday")
            for i in range(monthrange(Y, M)[1]):
                calendarRow.append(i + 1)
            if len(calendarRow) < 42:
                for i in range(42 - len(calendarRow)):
                    calendarRow.append("")
            calendarRow = np.array(calendarRow)
            calLayout = calendarRow.reshape(6, 7)
            print(calLayout)
            return calLayout

        createMonth(curYear, curMonth)
        def build_calGrid(calLayout):
            global calGrid
            calGrid = GridLayout(rows=7, cols=7)
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
                    if label == str(currentTime.strftime("%d")) and year == int(
                            currentTime.strftime("%Y")) and month == int(currentTime.strftime("%m")):
                        self.calElem = Button(text="[b][color=fc0303]{0}[/color][/b]".format(label), markup=True)
                        self.calElem.bind(on_press=on_elem_press)
                        calGrid.add_widget(self.calElem)
                    else:
                        self.calElem = Button(text=label)
                        self.calElem.bind(on_press=on_elem_press)
                        calGrid.add_widget(self.calElem)
            main_layout.add_widget(calGrid)
        build_calGrid(calLayout)
        return main_layout  # Return after all widgets are added

    def left_button_pressed(self, instance):
        global month, year
        month = month - 1
        if month == 0:
            year = year - 1
            month = 12
        createMonth(year, month)
        self.selectedMonth.text = str("{0} {1}".format(monthList[month - 1], year))
        main_layout.remove_widget(calGrid)
        build_calGrid(calLayout)

    def right_button_pressed(self, instance):
        global month, year
        month = month + 1
        if month == 12:
            year = year + 1
            month = 1
        createMonth(year, month)
        self.selectedMonth.text = str("{0} {1}".format(monthList[month - 1], year))
        main_layout.remove_widget(calGrid)
        build_calGrid(calLayout)


if __name__ == "__main__":
    app = MyApp()
    app.run()
