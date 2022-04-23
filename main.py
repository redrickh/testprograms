# You make a program that prompts the user on the command line
# for an input "guess a number between 1 and 10" and checks it against a
# randomly selected integer 1-10 and tells them if their guess is too high or too low.
# Game ends (program exits) when they guess the exact number. Complete this as I specified.
# If you get through and you want more you can make it 1-100, or make it keep track of how many guesses
# it takes the user to find the number, or persist the interaction history to a file.
import random

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import helpers
import usern

test = 0
rnum = random.randint(1, 100)


class DemoApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Green"
        screen = Screen()
        self.username = Builder.load_string(helpers.username_input)
        self.quess = Builder.load_string(usern.quess)
        button = MDRectangleFlatButton(text='Küldés',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)

        screen.add_widget(self.quess)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        global test

        print(rnum)

        if self.username.text == str(rnum):
            user_error = " Helyes válasz! Nyertél!"
        elif self.username.text > str(rnum):
            print("Nagyobb")
            user_error = "Kisebb szám lesz!"
            test += 1
            self.quess.text = str(test)

        elif self.username.text < str(rnum):
            print("Kisebb")
            user_error = "Nagyobb szám lesz!"
            test += 1
            self.quess.text = str(test)

        self.dialog = MDDialog(title='Nos...',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Bezár', on_release=self.close_dialog),
                                        ]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog


DemoApp().run()
