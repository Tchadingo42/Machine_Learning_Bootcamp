# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    maboy.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 15:57:46 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 16:54:54 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) != 2:
    print("ERROR")
    exit(-1)

text_analyzer = sys.argv[1]
size = len(text_analyzer)
print("The text contains [{}] characters" .format(size))
print("[{}]\n" .format(text_analyzer))

upper_value = 0
lower_value = 0
space = 0
punctuation = 0

for letter in text_analyzer:
    if letter.isupper():
        upper_value += 1
    elif letter.islower():
        lower_value += 1
    elif letter.isspace():
        space += 1
    elif letter in string.punctuation:
        punctuation += 1

print("[{}] upper letters\n" .format(upper_value))
print("[{}] lower letters\n" .format(lower_value))
print("[{}] spaces\n" .format(space))
print("[{}] punctuation letters\n" .format(punctuation))
