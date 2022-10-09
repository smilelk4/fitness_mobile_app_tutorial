from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

# must be after class declarations
GUI = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

if __name__ == "__main__":
    MainApp().run()