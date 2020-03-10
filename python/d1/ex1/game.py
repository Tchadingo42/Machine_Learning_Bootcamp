# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 11:59:54 by chbelan           #+#    #+#              #
#    Updated: 2020/03/10 13:20:24 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class GotCharacter:
    def __init__(self, first_name, is_alive: True):
        self.first_name = first_name
        self.is_alive = is_alive
        
class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False

p1 = GotCharacter("Chbelan", True)
print("{} {}\n" .format(p1.first_name, p1.is_alive))

from game import GotCharacter, Stark

arya = Stark("Arya", True)

print(arya.__dict__)
print(arya.is_alive)

arya.print_house_words()
arya.die()
print(arya.is_alive)
