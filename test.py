import random
name = input("what is your name> ")
colour = input("what is your favourite colour> ")

def colour_comp_checker(name, colour):
    colours = ["red", "blue", "green", "yellow", "purple", "orange"]
    computer_colour = random.choice(colours)
    print(f"Hello, {name}! Your favourite colour is {colour}.")
    print(f"The computer's favourite colour is {computer_colour}.")
    if colour == computer_colour:
        print(f"{name} and the computer have the same favourite colour!")
        return True
    else:
        print(f"{name} and the computer have different favourite colours.")
        return False

colour_comp_checker(name, colour)
