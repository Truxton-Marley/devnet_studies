#Tutorial from Criag Denis on https://teamtreehouse.com/
#with only minor changes.

TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:

    # Output how many tickets
    print("We currently only have {} tickets remaining! Act soon!".format(tickets_remaining))

    # Gather the user's name
    user = input("What's your name there, good person! ")

    try:
        requested_tickets = int(input("Hiya, {}, how many tickets are you after today? ".format(user)))
        if requested_tickets > tickets_remaining:
            raise ValueError("Not enough tickets")
    except ValueError as e:
        print("\nError, Error, Destroy, Destroy:")
        print(e + "\n")
        continue

    total_price = requested_tickets * TICKET_PRICE

    print("That'll be right about ${} there, pal.".format(total_price))

    # Prompt user if they want to continue
    keep_going = input("Would you like to continue: Y/n? ")
    # If they want to continue:
    if keep_going.lower().startswith("y"):
        # Confirm purchase and decrement tickets remaining
        print("Congrats on your purchase of {} tickets {}. Enjoy the show!".format(requested_tickets, user))
        tickets_remaining -= requested_tickets
    # Otherwise thank them and say goodbye
    else:
        print("Well, that's me. Bye now.")

else:
    print("Bummer, no more ticket for sale :( ")