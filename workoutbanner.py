from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import kivy.utils

class WorkoutBanner(GridLayout):
    rows = 1

    def __init__(self, **kwargs):
        super(WorkoutBanner, self).__init__()
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#67697C")))
            # at this point, rectangle size and pos are not properly set yet
            self.rectangle = Rectangle(size=self.size, pos=self.pos)
        # so, watch out for canvas pos and size changes, and call update_rectangle() then to update rectangle properties
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)

        left = FloatLayout()
        # sometimes, pos_hint of "left" causes overlapping issue so using "right"
        left_image = Image(source="icons/" + kwargs["workout_image"], size_hint=(1, .8), pos_hint={"top": 1, "right": 1})
        left.add_widget(left_image)
        left_label = Label(text=kwargs["description"], size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        left.add_widget(left_label)
        self.add_widget(left)

        middle = FloatLayout()
        middle_image = Image(source="icons/" + kwargs["type_image"], size_hint=(1, .8), pos_hint={"top": 1, "right": 1})
        middle.add_widget(middle_image)
        middle_label = Label(text=str(kwargs["value"]) + " " + kwargs["unit"], size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        middle.add_widget(middle_label)
        self.add_widget(middle)

        right = FloatLayout()
        right_image = Image(source="icons/likes.png", size_hint=(1, .8), pos_hint={"top": 1, "right": 1})
        right.add_widget(right_image)
        right_label = Label(text=str(kwargs["likes"]) + " likes", size_hint=(1, .2), pos_hint={"top": .2, "right": 1})
        right.add_widget(right_label)
        self.add_widget(right)

    # *args are coming from .bind()
    def update_rectangle(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size
