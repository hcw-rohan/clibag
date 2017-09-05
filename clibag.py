#!/usr/bin/python3
""" command line interface based adventure game """

from __future__ import print_function
import os
import json
import time
import sys
import requests
from colorama import init, deinit, Fore
init()

class Game(object):
    """ Entry point """
    api_gateway = 'http://127.0.0.1:5000/api/'
    text_speed = 3

    def __init__(self):
        """ Constructor """

        self.clear()

    @staticmethod
    def clear():
        """ clear the console """

        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def wait(seconds, char="_"):
        """ show a blinking dot """

        blink_time = 0.5
        blinks = int(seconds/blink_time)

        for i in range(0, blinks):
            if i == 0 or i % 2 == 0:
                sys.stdout.write(char+' ')
            else:
                sys.stdout.write('  ')

            sys.stdout.flush()
            sys.stdout.write('\b\b')
            time.sleep(blink_time)

        if seconds % blink_time != 0:
            if int(seconds/blink_time) % 2 == 0:
                sys.stdout.write(char+' ')
            else:
                sys.stdout.write('  ')

            sys.stdout.flush()
            sys.stdout.write('\b\b')
            time.sleep(seconds % blink_time)

    def get_question(self, qid):
        """ get question from api by id """
        r = requests.post(self.api_gateway, data={'qid':qid})
        return r.text

    def ask_question(self, json_string, speed=3, colour=Fore.RESET):
        """ ask the player a question """

        self.clear()
        json_object = json.loads(json_string)
        GAME.typeit(json_object['text'], speed, colour)
        self.wait(0.5)
        for choice in json_object['choices']:
            GAME.typeit(choice['label'], speed, colour)
            self.wait(0.5)

        correct_answer = False

        while correct_answer is False:
            answer = input('What is your choice? ')
            for choice in json_object['choices']:
                if answer.lower() == choice['answer']:
                    GAME.typeit(choice['response'], speed, colour)
                    self.wait(1)
                    return choice['result']

            GAME.typeit('I don\'t understand', speed, colour)
    
    def ask(self, question, colour=Fore.RESET):
        """ prompt for a response """
        return input(colour + question)

    def typeit(self, string, speed=3, colour=Fore.RESET):
        """ type out a string old school style """
        self.text_speed = speed
        for c in string:
            sys.stdout.write(colour + c)
            sys.stdout.flush()
            time.sleep(0.1/self.text_speed)
        
        sys.stdout.write('\n')
        sys.stdout.flush()

GAME = Game()

try:
    # Entry point
    GAME.typeit('Welcome to CLI BAG')
    GAME.wait(3)

    PLAYER_NAME = GAME.ask('Name yourself: ', Fore.WHITE)

    # Decision Tree demo
    GAME.typeit('Welcome to the game, '+PLAYER_NAME)
    GAME.wait(3)

    # Ask the first question
    RESULT = GAME.ask_question(GAME.get_question('0'))

    # Start the game loop
    while RESULT != 'null':
        RESULT = GAME.ask_question(GAME.get_question(int(RESULT) - 1))

except (KeyboardInterrupt):
    GAME.clear()
    GAME.typeit('Thanks for playing!', 5)
    deinit()
    pass