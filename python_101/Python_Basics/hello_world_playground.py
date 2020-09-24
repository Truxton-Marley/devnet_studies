# YAGNI
# KISS
# DRY
#Hello World, input, help:
print("Dzien Dobry!")

help(print)
info = input("Pass me some info: ")
len("yo")

#Super basic booleans:
"ham" in "hamster"

bool("quesadillas")
bool("")
bool(262)
bool(0)

not True

not False

True and True


#import math :)
import math
math.ceil(47.891)


#Murphy's Law
#a supposed law of nature, expressed in various humorous popular sayings,
#to the effect that anything that can go wrong will go wrong.

try:
    fav_num = int(input("What's a good number? "))
except ValueError:
    print("not a valid value")
else:
    print("You selected {}.".format(fav_num))


#########################################################################
########################   LISTS IN PYTHON   ############################
#########################################################################

letters = list("This cat is overweight")

letters.append("!")

letters.extend(list(" He needs to go on a diet.."))
letters.pop()
buchstaben = letters.copy()
letters.pop(0)
print("BUCHSTABEN:", "".join(buchstaben))


print(letters)
# Lists are mutable!!!
# Python recommends the trailing comma now

#python -i my_file.py


#########################################################################
#######################   TUPLES IN PYTHON   ############################
#########################################################################

# tuples defined by ,
# tuples are immutable

# A tuple without parens
groceries = 'apples', 'oranges', 'lettuce', 'cheddar cheese'

# A tuple with parens
groceries = ('apples', 'oranges', 'lettuce', 'cheddar cheese')


# A tuple is defined by the comma!
my_tuple = 73,

# The same tuple with parens
my_tuple = (73,)

#########################################################################
##################   PACKING/UNPACKING IN PYTHON   ######################
#########################################################################

def packer(*args):
    for i in args:
        print(i)

def calculate_total(*args):
    return sum(args)

def unpacker():
    return (1, 2, 3)

a, b, c = unpacker()

#first_name, last_name = input("Wie heissen Sie? \n").split(' ')

#########################################################################
######################   SEQUENCES IN PYTHON   ##########################
#########################################################################

my_list = ["kotek", "pinecone", "bones", "butter", "daisy", "barkmaster-b"]
for index, item in enumerate(my_list, 1):
    print(f'{index} is {item}')

for x in range(10):
    pass

# Reverse list
backwards_list = my_list[::-1]

# .reverse() <--in place

# len() min() max()

# mystr.index("looking for this")    <----Internalize!!! <--Returns ValueError when not in list
# mystr.count("counting this")



#########################################################################
########################   DICTS IN PYTHON   ############################
#########################################################################

# keys can be any immutable type (all items in tuple must be immutable too)
# values can be any type

#Some of the basic rules in Python are that:

#1) Uppercase letters come earlier than lowercase letters. This means that A < Z < a < z.

#2) Numbers come earlier than letters. This means that 0 < 9 < A < a.

#3) Space characters come before all printable characters.

my_dict = {"name":"Timmy"}

student = {"name": "Truxton", "topic": "python", "level": "basic"}

my_dict.keys()
my_dict.values()

sorted(my_dict.keys())

for k, v in student.items():
    print(k)
    print(student[k])
    print(v)

def print_kitty(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')


#########################################################################
##########################   DUNDER MAIN   ##############################
#########################################################################

if __name__ == "__main__":
    #do something
    pass







