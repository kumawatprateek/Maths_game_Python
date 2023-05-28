import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from random import randint, choice

# MathGame class represents the main game layout
class MathGame(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.level = 1  # Tracks the current level of the game
        self.score = 0  # Tracks the player's score
        self.character_pos = 0  # Tracks the position of the character

        # Title label
        self.title_label = Label(text="Math Game", font_size=40, size_hint_y=None, height=100)
        self.add_widget(self.title_label)

        # Level label
        self.level_label = Label(text="Level: {}".format(self.level), font_size=20, size_hint_y=None, height=50)
        self.add_widget(self.level_label)

        # Question label
        self.question_label = Label(text="", font_size=25, size_hint_y=None, height=50)
        self.add_widget(self.question_label)

        # Answer input
        self.answer_input = TextInput(multiline=False, font_size=25, size_hint_y=None, height=50)
        self.add_widget(self.answer_input)

        # Submit button
        self.submit_button = Button(text="Submit", font_size=25, size_hint_y=None, height=50)
        self.submit_button.bind(on_release=self.check_answer)
        self.add_widget(self.submit_button)

        # Result label
        self.result_label = Label(text="", font_size=25, size_hint_y=None, height=50)
        self.add_widget(self.result_label)

        # Character label
        self.character_label = Label(text="Character", font_size=30, size_hint_y=None, height=100)
        self.add_widget(self.character_label)

        # Move layout
        self.move_layout = GridLayout(cols=2, size_hint_y=None, height=100)
        self.add_widget(self.move_layout)

        # Move left button
        self.move_left_button = Button(text="Move Left", font_size=20)
        self.move_left_button.bind(on_release=self.move_left)
        self.move_layout.add_widget(self.move_left_button)

        # Move right button
        self.move_right_button = Button(text="Move Right", font_size=20)
        self.move_right_button.bind(on_release=self.move_right)
        self.move_layout.add_widget(self.move_right_button)

        self.generate_question()  # Generate the initial question

    def generate_question(self):
        # Generates a new math question
        num1 = randint(1, 10 + self.level * 5)
        num2 = randint(1, 10 + self.level * 5)
        operator = choice(["+", "-", "*"])
        self.answer = str(eval(f"{num1} {operator} {num2}"))
        self.question_label.text = f"What is {num1} {operator} {num2}?"

    def check_answer(self, instance):
        # Checks the player's answer
        player_answer = self.answer_input.text

        if player_answer == self.answer:
            self.result_label.text = "Correct! Proceed to the next level."
            self.score += 1
            self.level += 1
            self.level_label.text = "Level: {}".format(self.level)
        else:
            self.result_label.text = "Incorrect answer. Try again."

        self.character_pos = self.score % 10
        self.character_label.text = "Character" + " " * self.character_pos

        self.answer_input.text = ""
        self.generate_question()

    def move_left(self, instance):
        # Moves the character to the left
        if self.character_pos > 0:
            self.character_pos -= 1
            self.character_label.text = "Character" + " " * self.character_pos

    def move_right(self, instance):
        # Moves the character to the right
        if self.character_pos < self.score % 10:
            self.character_pos += 1
            self.character_label.text = "Character" + " " * self.character_pos

# MathGameApp class represents the Kivy application
class MathGameApp(App):
    def build(self):
        return MathGame()

if __name__ == '__main__':
    MathGameApp().run()

# Author: Prateek
# This code was originally written by Prateek.
# Copyright (c) Prateek, 2023. All rights reserved.