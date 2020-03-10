# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    example.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 17:40:59 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 18:43:30 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

if len(argv) == 1:
    print("Usage: python operations.py")
    print("Example:")
    print("python operations.py 10 3")
elif len(argv) == 3:
    try:
        my_sum = int(argv[1]) + int(argv[2])
        my_diff = int(argv[1]) - int(argv[2])
        my_mul = int(argv[1]) * int(argv[2])
        if int(argv[2]) != 0:
            my_div = int(argv[1]) / int(argv[2])
            my_mod = int(argv[1]) % int(argv[2])
        else:
            my_div = "ERROR (div by zero)"
            my_mod = "ERROR (modulo by zero)"
        print(f'Sum:\t\t {my_sum}\n'
              f'Difference:\t {my_diff}\n'
              f'Product:\t {my_mul}\n'
              f'Quotient:\t {my_div}\n'
              f'Remainder:\t {my_mod}')
    except ValueError:
        print("InputError: only numbers")
        print("Usage: python operations.py")
        print("Example:")
        print("python operations.py 10 3")
elif len(argv) > 3:
    print("InputError: too many arguments")
    print("Usage: python operations.py")
    print("python operations.py 10 3")
elif len(argv) == 2:
    print("InputError: too few arguments")
    print("Usage: python operations.py")
    print("python operations.py 10 3")
