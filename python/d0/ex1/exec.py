# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 11:24:26 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 13:31:54 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# list[x] -> print element index x
# list[-x] -> print x th elem from the end
# list[:] -> print all elements
# list[:x] -> print the x th first elements
# list[x:] -> print the x th last elements 
# range sequence of numbers
#x = range(6)
#for n in x:
#    print(n)
# parsing in the sequence
#x = range(3, 6)
#for n in x:
#    print(n)
import  sys

my_str = sys.argv[1]
my_str = my_str[::-1]
print(my_str)
