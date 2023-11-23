# a program that converts your name into a Star Wars name
# provide background info such as Religion, Home Planet, Light Saber Colour
import random
import sys
import turtle


def get_name():
    name = None
    accept_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    while name is None:
        name = input("Enter your full name: ").lower()
        if name[0] not in accept_list:
            print("Invalid Entry, please enter a valid name")
        else:
            return name


def assign_SW_name(name):
    first_sw_name = ""
    second_sw_name = ""
    ai = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    jo = ["j", "k", "l", "m", "n", "o"]
    nw = ["q", "r", "s", "t", "u", "v", "w"]
    xz = ["x", "y", "z"]

    if name[0] in ai:
        first_sw_name = "Master "
    elif name[0] in jo:
        first_sw_name = "Darth "
    elif name[0] in nw:
        first_sw_name = "Padawan "
    else:
        first_sw_name = "Sith Lord "

    if len(name) <= 3:

        if name[1] in ai:
            second_sw_name = "Kython"
        elif name[1] in jo:
            second_sw_name = "Varian"
        elif name[1] in nw:
            second_sw_name = "Xandor"
        elif name[1] in xz:
            second_sw_name = "Skysinger"
        else:
            second_sw_name = "Skywalker"

    elif len(name) <= 5:

        if name[2] in ai:
            second_sw_name = "Driftwood"
        elif name[2] in jo:
            second_sw_name = "Malachai"
        elif name[2] in nw:
            second_sw_name = "Naloria"
        elif name[2] in xz:
            second_sw_name = "Kelobi"
        else:
            second_sw_name = "Mindo"

    elif len(name) <= 7:

        if name[3] in ai:
            second_sw_name = "Starfury"
        elif name[3] in jo:
            second_sw_name = "Vortexia"
        elif name[3] in nw:
            second_sw_name = "Shadowheart"
        elif name[3] in xz:
            second_sw_name = "Sirius"
        else:
            second_sw_name = "Ish-Luca"

    elif len(name) > 7:
        if name[5] in ai:
            second_sw_name = "Zenithar"
        elif name[5] in jo:
            second_sw_name = "Stratos"
        elif name[5] in nw:
            second_sw_name = "Nimbus"
        elif name[5] in xz:
            second_sw_name = "Vlakorian"
        else:
            second_sw_name = "Astralynn"

    sw_name = first_sw_name + second_sw_name
    return sw_name


def assign_religion(sw_name):
    religion = ""
    if sw_name[0] == "S" or sw_name[0] == "D":
        religion = "Sith"
    elif sw_name[0] == "M" or sw_name[0] == "P":
        religion = "Jedi"
    else:
        religion = None
    return religion


def assign_saber_colour(religion):
    jedi_colours = ["Green", "Blue", "Purple", "Pink", "White"]
    additional_colors = ["Yellow", "Orange", "Teal", "Magenta", "Cyan", "Lavender", "Maroon", "Turquoise", "Amber",
                         "Indigo"]

    saber = ""
    if religion == "Jedi":
        saber = random.choice(jedi_colours)
    elif religion == "Sith":
        saber = "Red"
    else:
        saber = random.choice(additional_colors)
    return saber


def assign_home_planet():
    planets = [
        "Tatooine", "Coruscant", "Endor", "Hoth", "Naboo",
        "Kashyyyk", "Mustafar", "Dagobah", "Jakku", "Kamino",
        "Geonosis", "Alderaan", "Yavin IV", "Bespin", "Sullust",
        "Mandalore", "Ryloth", "Felucia", "Kessel", "Mon Cala",
        "Felucia", "Mygeeto", "Polis Massa", "Dantooine", "Korriban",
        "Ilum", "Ord Mantell", "Dathomir", "Lothal", "Umbara",
        "Mimban", "Rishi", "Saleucami", "Raxus Prime", "Christophsis",
        "Muunilinst", "Hoth", "Kamino", "Malachor", "Mandalore"
    ]
    planet = random.choice(planets)
    return planet


def print_results(name, sw_name, religion, saber, planet):
    name = name.upper()
    print(f"You used to be known as {name}")
    print(f"Now you are reborn as {sw_name} of the {religion}")
    print(f"You acquired a {saber} LightSaber when you left your home planet of {planet}")


def extend_saber(saber):
    # turtle.speed(1)
    # turtle.penup()
    # turtle.goto(-100, 0)
    # turtle.pendown()
    # turtle.pensize(10)
    # turtle.pencolor(saber)
    # turtle.forward(200)
    # turtle.bye()
    pass


def retract_saber():
    pass


def main():
    while True:
        name = get_name()
        sw_name = assign_SW_name(name)
        religion = assign_religion(sw_name)
        saber = assign_saber_colour(religion)
        planet = assign_home_planet()
        extend_saber(saber)
        print_results(name, sw_name, religion, saber, planet)

        choice = input("Would you like try another name? Y/N: ")
        if choice.lower() == "y":
            main()
        elif choice.lower() == "n":
            print(f"Exiting Program, {sw_name}")
            retract_saber()
            sys.exit()


main()
