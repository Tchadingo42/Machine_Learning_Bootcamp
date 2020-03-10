# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 20:33:06 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 22:26:14 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# create dictionary 
# dico {} # empty
# dico {<key>:<value>, <key2><value>}
# acces to value dico[<key>]

#dico = {"student": "chbelan"}
#print(dico)

first_str = "abc"
second_str = "ghi"

string = "abcdef"

print("orignal", string)

translation = string.maketrans(first_str, second_str)

print("Translated string:", string.translate(translation))
