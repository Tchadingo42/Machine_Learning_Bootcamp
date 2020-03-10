# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 13:15:21 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 16:53:34 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) != 2:
    print("ERROR")
    exit(-1)

text = sys.argv[1]

    upper_value = 0
    lower_valuer = 0
    space_value = 0
    ponct = 0
    size = len(text)

    for letter in text:
        if letter.isupper():
            upper_value += 1
        elif letter.islower():
            lower_value += 1
        elif letter.isspace():
            space += 1
        elif letter in string.punctuation:
            punct += 1

print("- {} upper letters\n" .format(upper_value))
print("- {} lower letters\n" .format(lower_value))
print("- {} punctuation letters\n" .format(punct))
print("- {} spaces\n" .format(space))
