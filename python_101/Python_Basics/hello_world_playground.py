print("Dzien Dobry!")

help(print)

info = input("Pass me some info: ")

len("yo")

"ham" in "hamster"

bool("quesadillas")
bool("")
bool(262)
bool(0)


not True

not False

True and True



import math
math.ceil(47.891)


#Murphy's Law
#a supposed law of nature, expressed in various humorous popular sayings,
#to the effect that anything that can go wrong will go wrong.

try:
    input = int("What's a good number? ")
except ValueError:
    print("not a valid value")