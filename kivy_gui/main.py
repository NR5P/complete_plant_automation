"""
gui for raspberry pi touchscreen
"""

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('1.10.1')

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        Clock.schedule_interval(self.printSomething, 1)

    def sayHello(self, this):
        self.add_widget(Button(text="something else"))

    def printSomething(self, this):
        print("soemthing")

class ComponentList(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")


class MainApp(App):
    #def updateFromJson(self):
        #Clock.schedule_interval(printSomething, 0.5)

    def build(self):
        return kv

if __name__ == "__main__":
    MainApp().run()