# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bank.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 15:26:23 by chbelan           #+#    #+#              #
#    Updated: 2020/03/10 18:48:53 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0      
        Account.ID_COUNT += 1
