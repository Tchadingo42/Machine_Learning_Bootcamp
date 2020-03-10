# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwrods.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 20:55:49 by chbelan           #+#    #+#              #
#    Updated: 2020/03/10 13:17:41 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
import string

if len(argv) != 3:
    print("ERROR")
    exit(-1)
else:
    argv[2] = int(argv[2])
    if not (isinstance(argv[1], str) and isinstance(argv[2], int)):
        print("ERROR")
    if str.isdigit(argv[1]):
        print("ERROR")
    else:
        my_list = argv[1].split()
        my_list = [words.translate(str.maketrans('', '', string.punctuation))
                  for words in my_list if (len(words) > argv[2])]
        print(my_list)
