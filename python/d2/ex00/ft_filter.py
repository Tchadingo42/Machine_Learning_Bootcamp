# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 10:50:30 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 15:21:40 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#creates a list of elements for which a function returns true

def ft_filter(function_to_apply,list_of_inputs):
    res=[]
    for i in list_of_inputs:
        if function_to_apply(i):
            res.append(i)
    return res

def is_even(item):
    if item%2==0 :
        return True
    else :
        return False



seq=[1,2,3,4,5,6,7,8,9,10]
print(ft_filter(is_even,seq))
