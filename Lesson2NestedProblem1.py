#Task 1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action=="cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!")
else:
    pass


#Task 2
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action=="cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action2 = input("light a torch or proceed in the dark?")
    if action2 == "light a torch":
        print("You successfully navigate over a hole!")
    elif action2=="proceed in the dark":
        print("You fall in a hole and die.")
    else:
        pass
else:
    pass


#Task 3
#Added the 'pass' options to the prior tasks

