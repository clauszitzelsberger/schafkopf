# -*- coding: utf-8 -*-

import numpy as np

numbers = ['siebener',
          'achter',
          'neuner',
          'zehner',
          'unter',
          'ober',
          'koenig',
          'sau']

values = [0, 0, 0, 10, 2, 3, 4, 11]

colors = ['eichel', 'gras', 'herz', 'schellen']

def initialize(id):
    # Id and one hot encoded id
    one_hot = np.zeros(32)
    one_hot[id] = 1

    # Color and number
    if id < 8:
        color = colors[0]
    elif id < 16:
        color = colors[1]
    elif id < 24:
        color = colors[2]
    else:
        color = colors[3]
    number = numbers[id%8]

    # Value of card
    value = values[id%8]

    # Display name
    name = (color + ' ' + number)

    # Distinguish betwenn Unter+Ober and rest of cards
    if number in ['unter', 'ober']:
        not_ober_unter = False
    else:
        not_ober_unter = True

    card = {'id': id,
            'one_hot': one_hot,
            'color': color,
            'number': number,
            'value': value,
            'name': name,
            'not_ober_unter': not_ober_unter
            }
    return card
