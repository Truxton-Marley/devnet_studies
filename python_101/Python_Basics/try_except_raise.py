import sys

def feed_cat(cat):
    if cat.lower() == "daisy":
        raise ValueError("But you're a dog!")
    return "cat fed"


cat = input("Which critter needs food? ")

try:
    feed_cat(cat)
except ValueError as err:
    print("{}".format(err))
    sys.exit("Someone tried to give Daisy cat food :| ")