# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chbelan <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 15:45:53 by chbelan           #+#    #+#              #
#    Updated: 2020/03/11 18:34:15 by chbelan          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Price:
    firm = "Nintendo"
    standard_price = 60
    online_price = 45

e = Price()
print(getattr(e, 'standard_price', 50))
setattr(e, 'standard_price', 70)
#print(getattr(e, 'new_price', 50))
print(getattr(e, 'new_price', e.online_price))
print(e.standard_price)

print("-- test hasattr --")
class Person:
    age = 22
    name = 'chris'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))

print("-- test *argv, **kwargs --")


def multiply(*args):
    n = 1
    for i in args:
        n *= i
    print(n)

multiply(3, 3, 3, 3)
print("-- test **kwargs --")

car = {"Brand": "Ford", "Model":"Mustang", "year": 1964}
x = car.items()
#car["year"] = 2018
print(x)

print("-- Print elem check by items() --")
print(x)
print()

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}" .format(key, value))

print_values(arg1="chris", arg2="tchadingo")
