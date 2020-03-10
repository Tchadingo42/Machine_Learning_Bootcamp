# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 12:10:00 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 15:08:13 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
    print("ERROR")
    exit(-1)

try:
    value = int(sys.argv[1])
    if value == 0:
        print("I'm zero")
    elif value % 2 != 0:
        print("I'm odd")
    else:
        print("I'm Even")
except ValueError:
    print("ERROR")
