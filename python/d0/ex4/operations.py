# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 16:57:41 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 18:24:49 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) >= 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("python operations.py 10 3")
    
    if len(sys.argv) == 3:
        try:
            my_sum = int(sys.argv[1]) + int(sys.argv[2])
            my_dif = int(sys.argv[1]) - int(sys.argv[2])
            my_pro = int(sys.argv[1]) * int(sys.argv[2])
            if int(sys.argv[2]) != 0:
                my_quo = int(sys.argv[1]) / int(sys.argv[2])
                my_mod = int(sys.argv[1]) % int(sys.argv[2])
            else:
                my_quo = "ERROR (div by zero)"
                my_mod = "ERROR (modulo)"
                print("Sum:\t {}\n" .format(my_sum))
                print("Difference:\t {}\n" .format(my_dif))
                print("Product:\t {}\n" .format(my_pro))
                print("Quotient:\t {}\n" .format(my_quo))
                print("Modulot:\t {}\n" .format(my_mod))
        except ValueError:
            print("Usage: python operations.py <number1> <number2>")
            print("Example")
            print("python operations.py 10 3")
       # elif len(sys.argv) > 3:
       #    print("InputError: too many arguments")
       #   print("Example")
       #  print("python operations.py 10 3")
