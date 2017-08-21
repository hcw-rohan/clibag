#!/usr/bin/python3
""" command line interface based adventure game """

from __future__ import print_function
import os
import time
import sys
import json

class Game(object):
    """ Entry point """
    json_data = ''

    def __init__(self):
        """ Constructor """

        self.clear()

    def load_json(self, filename):
        """ load external json file """

        with open(filename) as data_file:
            self.json_data = json.load(data_file)

    @staticmethod
    def clear():
        """ clear the console """

        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def wait(seconds):
        """ show a blinking dot """

        blink_time = 0.5
        blinks = int(seconds/blink_time)

        for i in range(0, blinks):
            if i == 0 or i % 2 == 0:
                sys.stdout.write('. ')
            else:
                sys.stdout.write('  ')

            sys.stdout.flush()
            sys.stdout.write('\b\b')
            time.sleep(blink_time)

        if seconds % blink_time != 0:
            if int(seconds/blink_time) % 2 == 0:
                sys.stdout.write('. ')
            else:
                sys.stdout.write('  ')

            sys.stdout.flush()
            sys.stdout.write('\b\b')
            time.sleep(seconds % blink_time)

    def ask_question(self, json_string):
        """ ask the player a question """

        self.clear()
        json_object = json.loads(json_string)
        print(json_object['text'])
        self.wait(0.5)
        for choice in json_object['choices']:
            print(choice['label'])
            self.wait(0.5)

        correct_answer = False

        while correct_answer is False:
            answer = input('What is your choice? ')
            for choice in json_object['choices']:
                if answer.lower() == choice['answer']:
                    print(choice['response'])
                    return choice['result']

            print('I don\'t understand')

GAME = Game()
GAME.load_json("dummy.json")

# Entry point
print('Welcome to CLI BAG')
GAME.wait(3)

PLAYER_NAME = input('Name yourself: ')

# Decision Tree demo
print('Here\'s an introductory message')
GAME.wait(2)

# Get the questions
QUESTIONS = GAME.json_data['questions']

# Ask the first question
RESULT = GAME.ask_question(json.dumps(QUESTIONS[0]))

# Start the game loop
while RESULT != 'null':
    RESULT = GAME.ask_question(json.dumps(QUESTIONS[int(RESULT) - 1]))
