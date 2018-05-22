from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 

class MainScreen(Screen):
    pass

class LightsScreen(Screen):
    pass

class ValvesScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

#class IrrigationGUI(GridLayout):
#    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name="main"))
sm.add_widget(SettingsScreen(name="settings"))
sm.add_widget(LightsScreen(name="lights"))
sm.add_widget(ValvesScreen(name="valves"))
sm.current = "main"

class IrrigationGUIApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    IrrigationGUIApp().run()
