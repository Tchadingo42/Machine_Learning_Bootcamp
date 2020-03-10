# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 18:56:12 by chbelan           #+#    #+#              #
#    Updated: 2020/03/09 19:08:58 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

l = {'Python': 'Guido van Rossum', 'Ruby': 'Yukihiro Matsumoto', 'PHP': 'Rasmus Lerdorf',}

for i,j in l.items():
    print("{} was create by {}" .format(i,j))
