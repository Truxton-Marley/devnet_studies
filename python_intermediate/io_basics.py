import sys

def jogger(forgettable):
    # r: read, w: clobber and write, a: append, x: fail if file exists
    file = open("things_to_remember.txt", "a")
    file.write(f'{forgettable}\n')
    file.close()

def jogger_v2(forgettable):
    """Add items that might be forgotten to a list file"""
    with open("things_to_remember.txt", "a") as file:
        file.write(f'{forgettable}\n')

def show():
    """Display items that have been added to the list"""
    with open("things_to_remember.txt") as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    if sys.argv[1].lower() == "--list":
        show()
    elif sys.argv[1].lower() == "--clear":
        pass
    else:
        jogger(input("Don't forget:\n"))
