from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import requests
import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Application Default credentials are automatically created.
cred = credentials.Certificate("firebaseServiceKey.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

# must be after class declarations
GUI = Builder.load_file("main.kv")

class MainApp(App):
    my_friend_id = 1;

    def build(self):
        return GUI

    def on_start(self):
        result = requests.get("https://firestore.googleapis.com/v1/projects/friendly-fitness-626ae/databases/(default)/documents")
        # result = requests.get(f"https://friendly-fitness-626ae.firebaseio.com/{self.my_friend_id}.json")
        print(result)

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

if __name__ == "__main__":
    MainApp().run()