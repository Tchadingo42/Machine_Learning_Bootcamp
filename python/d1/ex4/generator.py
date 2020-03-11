# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 17:12:32 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 10:53:49 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def generator(text, sep=" ", option=None):
    if not isinstance(text, str):
        return 'ERROR'
    if option and option not in ['shuffle', 'unique', 'ordered']:
        return 'ERROR'
    if option == 'shuffle':
        textlist = text.split(sep=sep)
        random.shuffle(textlist)
        for elem in textlist:
            yield elem
        pass
    elif option == 'unique':
        textlist = text.split(sep=sep)
        myset = set(textlist)
        textlist = list(myset)
        for elem in textlist:
            yield elem
    elif option == 'ordered':
        textlist = (text.split(sep=sep))
        textlist = sorted(textlist, key=str.lower)
        for elem in textlist:
            yield elem
    elif option is None:
        textlist = text.split(sep=sep)
        for elem in textlist:
            yield elem


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
    print(word)
