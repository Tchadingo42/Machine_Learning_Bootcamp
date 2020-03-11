# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 10:50:15 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 15:10:35 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import functools

lis = [ 1 , 3, 5, 6, 2, ]

print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,lis))

print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))

x = lambda a : a + 10
print(x(5))

y = lambda b : b * 10
print(y(1))


#def ft_reduce(function_to_apply, list_of_inputs):
#    for i in list_of_input:
#        elem = function_to_apply(elem, i)
#        return (elem)

def my_reduce(func, seq):
    first = seq[0]
    for i in seq[1:]:
        first = func(first, i)
        return first

