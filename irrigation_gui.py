from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class MainScreen(Screen):
    pass

class LightsScreen(Screen):
    pass

class ValvesScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

#class IrrigationGUI(GridLayout):
#    pass

class IrrigationGUIApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    IrrigationGUIApp().run()
