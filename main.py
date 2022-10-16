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

from workoutbanner import WorkoutBanner

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
    my_friend_id = "1"

    def build(self):
        return GUI

    def on_start(self):
        user = db.collection("friendly-fitness").document("friendly-fitness").get().to_dict()[self.my_friend_id]

        avatar_image = self.root.ids["home_screen"].ids["avatar_image"]
        avatar_image.source = "icons/" + user["avatar"]

        streak_label = self.root.ids["home_screen"].ids["streak_label"]
        streak_label.text = str(user["streak"]) + " Day Streak"

        workout_ids = user["workouts"]
        for workout_id in workout_ids:
            # just a quick hack of populating a bunch of rows
            for i in range(5):
                workout = workout_ids[workout_id]
                workout_banner = WorkoutBanner(**workout)
                # workout_banner = WorkoutBanner(workout_image=workout["workout_image"], description=workout["description"])
                self.root.ids["home_screen"].ids["banner_grid"].add_widget(workout_banner)

        # for doc in db_items:
        #     print(doc.to_dict())

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

if __name__ == "__main__":
    MainApp().run()