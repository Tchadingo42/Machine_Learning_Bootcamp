# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 10:49:47 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 15:38:22 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# map method launch function in every index of the list
# append push element at the end of the list

def addition(n):
    return n + n

my_list = (5, 10, 15, 2)
values = map(addition, my_list)

print(list(values))

my_list2 = ['Tchadingo', 'is']
my_list2.append('in')
#print(list(my_list2))

def ft_map(function_to_apply, list_of_inputs):
    values = []
    i = 0
    lenght = len(list_of_inputs)
    while i < lenght:
        for n in list_of_inputs:
            values.append(function_to_apply(n))
            n += 1
        i += 1
        return (values)

def multiplication(n):
    return n * 10

test_list = (2, 4, 8, 16)
lenght = len(test_list)
test = ft_map(multiplication, test_list)
print("-- test ft_map --")
print(list(test))
