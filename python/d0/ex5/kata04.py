# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 19:33:43 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 20:27:30 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = (0, 4, 132.42222, 10000, 12345.67)

#print(f'day_{t[0]:0>2}, ex_{t[1]:0>2} : {t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}')
# value -> day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
# t[0]: >2 add 2 times 0 value at the end of the array
# t[1]:.2f set the nbr of float values after the ,
# t[2]:.2e Converts to a floating point in exponential notation

print(f'day_{t[0]:0>2}, ex_{t[1]:0>2} : {t[2]:.4f}, {t[3]:.2e}, {t[4]:.2e}')
