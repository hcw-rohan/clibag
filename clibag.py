
""" command line interface based adventure game """

import time
import sys
import json

def wait(seconds):
    """ show a blinking dot """

    return

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

print('Welcome to CLI BAG')
wait(3)

player_name = input('Name yourself: ')

# Decision Tree demo
print('Here\'s an introductory message')
wait(2)

question1 = {
    'text': 'You have a choice: ',
    'choices': [
        {
            'label' : 'A: Do this',
            'answer' : 'a',
            'response' : 'You chose a',
            'result' : 1
        },
        {
            'label' : 'B: Do this',
            'answer' : 'b',
            'response' : 'You chose b',
            'result' : 2
        },
        {
            'label' : 'C: Do this',
            'answer' : 'c',
            'response' : 'You chose c',
            'result' : 3
        }
    ]
}

question2 = {
    'text': 'You have another choice: ',
    'choices': [
        {
            'label' : 'A: Do this',
            'answer' : 'a',
            'response' : 'You chose a',
            'result' : 'null'
        },
        {
            'label' : 'B: Do this',
            'answer' : 'b',
            'response' : 'You chose b',
            'result' : 'null'
        },
        {
            'label' : 'C: Do this',
            'answer' : 'c',
            'response' : 'You chose c',
            'result' : 'null'
        }
    ]
}

question3 = {
    'text': 'You have a third choice: ',
    'choices': [
        {
            'label' : 'A: Do this',
            'answer' : 'a',
            'response' : 'You chose a',
            'result' : 'null'
        },
        {
            'label' : 'B: Do this',
            'answer' : 'b',
            'response' : 'You chose b',
            'result' : 'null'
        },
        {
            'label' : 'C: Do this',
            'answer' : 'c',
            'response' : 'You chose c',
            'result' : 'null'
        }
    ]
}

question_bank = [question1, question2, question3]

def ask_question(json_string):
    json_object = json.loads(json_string)
    print(json_object['text'])
    wait(0.5)
    for choice in json_object['choices']:
        print(choice['label'])
        wait(0.5)

    correct_answer = False

    while correct_answer == False:
        answer = input('What is your choice? ')
        for choice in json_object['choices']:
            if answer.lower() == choice['answer']:
                print(choice['response'])
                return choice['result']
                correct_answer = True
                break
        
        if correct_answer == False:
            print('I don\'t understand')

question_json = json.dumps(question_bank[0])

# Ask the first question
result = ask_question(question_json)

# Start the game loop
while result != 'null':
    result = ask_question(json.dumps(question_bank[int(result) - 1]))