# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 18:01:14 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 10:53:27 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
    def zip_evaluate(coefs, words):
        res = 0
        if isinstance(words, list) and isinstance(coefs, list):
            if len(words) == len(coefs):
                for one, two in zip(words, coefs):
                    res += len(one) * two
                print(res)
            else:
                print(-1)
        else:
            print(-1)

    def enumerate_evaluate(coefs, words):
        res = 0
        if isinstance(words, list) and isinstance(coefs, list):
            if len(words) == len(coefs):
                for i, one in enumerate(words):
                    res += len(one) * coefs[i]
                    print(res)
            else:
                print(-1)
        else:
             print(-1)
