# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 18:10:41 by chbelan           #+#    #+#              #
#    Updated: 2020/03/10 18:47:31 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "Simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print("-- zip evaluate --\n")
Evaluator.zip_evaluate(coefs, words)


words_2 = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs_2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print("-- enumerate evaluate --\n")
Evaluator.enumerate_evaluate(coefs_2, words_2)
