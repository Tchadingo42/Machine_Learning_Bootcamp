# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 19:20:30 by chbelan           #+#    #+#              #
#    Updated: 2020/03/10 20:05:02 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

tmp = 0

print("Just take a look to the random function ")
print(random.random())

tmp = random.random()
print(tmp)

my_list = [2,5,6,9,12]
random.shuffle(my_list)
print(my_list)

print("-- generic fucntion --")

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

tmp = 42
tmp = my_gen()
print(tmp)
