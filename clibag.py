#!/usr/bin/python3
""" command line interface based adventure game """

from __future__ import print_function
import os
import json
import time
import sys
import requests

class Game(object):
    """ Entry point """
    api_gateway = 'http://127.0.0.1:5000/api/'

    def __init__(self):
        """ Constructor """

        self.clear()

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

    def get_question(self, qid):
        r = requests.post(self.api_gateway, data={'qid':qid})
        return r.text

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

# Entry point
print('Welcome to CLI BAG')
GAME.wait(3)

PLAYER_NAME = input('Name yourself: ')

# Decision Tree demo
print('Here\'s an introductory message')
GAME.wait(2)

# Ask the first question
RESULT = GAME.ask_question(GAME.get_question('0'))

# Start the game loop
while RESULT != 'null':
    RESULT = GAME.ask_question(GAME.get_question(int(RESULT) - 1))
