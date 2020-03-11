# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 16:14:13 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 18:35:44 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def what_are_the_vars(*args, **kwargs):
    my_object = ObjectC()
    for i, j in enumerate(args):
        setattr(my_object, 'var_' + str(i), j)
    for key, val in kwargs.items():
        if hasattr(my_object, key):
            return None
        setattr(my_object, key, val)
    return (my_object)

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(my_obj):
    if my_obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(my_obj):
        if attr[0] != '_':
            value = getattr(my_obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
