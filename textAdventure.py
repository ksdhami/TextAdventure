import constant

# Input Validation


def input_valid1(choice):
    if choice in ('1'):
        input_needed = False
    else:
		print(constant.ERROR_STR, choice, 'is not a valid choice. Select 1.\n')
		# print('\nERROR:', choice, 'is not a valid choice. Select 1.\n')
		input_needed = True
    return choice


def input_valid2(choice):
    if choice in ('1', '2'):
        input_needed = False
    else:
		print(constant.ERROR_STR, choice, 'is not a valid choice. Select 1, or 2.\n')
		# print('\nERROR:', choice, 'is not a valid choice. Select 1, or 2.\n')
		input_needed = True
    return choice


def input_valid3(choice):
    if choice in ('1', '2', '3'):
        input_needed = False
    else:
		print(constant.ERROR_STR, choice, 'is not a valid choice. Select 1, 2, or 3.\n')
		# print('\nERROR:', choice, 'is not a valid choice. Select 1, 2, or 3.\n')
		input_needed = True
    return choice


def input_valid4(choice):
    if choice in ('1', '2', '3', '4'):
        input_needed = False
    else:
		print(constant.ERROR_STR, choice, 'is not a valid choice. Select 1, 2, 3, or 4.\n')
		# print('\nERROR:', choice, 'is not a valid choice. Select 1, 2, 3, or 4.\n')
		input_needed = True
    return choice

# Kitchen


def kitchen(door_locked, current_dial, current_lever):
    input_needed = True
    while input_needed:
        print('\nRoom: Kitchen'+ constant.DIVIDER_STR)
        print('You are in the Kitchen which has all kinds of appliances to prepare food with. You see in front of you a lever that can be pushed forward or pulled back. Behind you is the door back to the entrance room.')
        print('\n- The lever is currently set to', current_lever, '-')
        print('Actions:'+'\n1) Push the lever forward' + '\n2) Pull the lever back'+'\n3) Go back to the Entrance Room')
        choice = input(constant.CHOICE_STR)
        choice = input_valid3(choice)

        if choice == '1':
            current_lever = 'forward'
            door_locked = True
            input_needed = True
        elif choice == '2':
            current_lever = 'back'
            door_locked = False
            input_needed = True
        elif choice == '3':
            input_needed = False
    return current_lever

# Pantry


def pantry(door_locked, current_dial, current_lever):
	input_needed = True
	print('\nRoom: Pantry'+constant.DIVIDER_STR)
	print('You are in the Pantry which contains all kinds of food. You see in front of you a dial that you can turn to 3 possible settings: blue, red, and green. Behind you is the door back to the entrance room.')
	while input_needed:
		print('\n- The dial is currently set to', current_dial, '-')
		print(constant.ACTIONS_STR +'\n1) Turn the dial to blue'+'\n2) Turn the dial to red' + '\n3) Turn the dial to green'+'\n4) Go back to the Entrance Room')
		choice = input(constant.CHOICE_STR)
		choice = input_valid4(choice)

		if choice == '1':
			current_dial = 'blue'
			door_locked = True
			input_needed = True
		elif choice == '2':
			current_dial = 'red'
			door_locked = False
			input_needed = True
		elif choice == '3':
			current_dial = 'green'
			door_locked = True
			input_needed = True
		elif choice == '4':
			input_needed = False
	return current_dial

# Entrance


def entryway(door_locked, current_dial, current_lever):
	print('\nRoom: Entrance Room'+constant.DIVIDER_STR)
	print('In front of you is a door that leads to the rest of the house. To your left is the Kitchen. To your right is the Pantry')
	while door_locked == True:
		print(constant.ACTIONS_STR +'\n1) Try to open the door' +'\n2) Go to your left and into the Kitchen'+'\n3) Go to your right and into the Pantry')
		input_needed = True
		choice = input(constant.CHOICE_STR)
		choice = input_valid3(choice)

		if choice == '1':
			if (current_lever == 'back') and (current_dial == 'red'):
				door_locked = False
			else:
				print('\n- The door is locked -')
		elif choice == '2':
			current_lever = kitchen(door_locked, current_dial, current_lever)
		elif choice == '3':
			current_dial = pantry(door_locked, current_dial, current_lever)
	return door_locked

# Attic


def attic(dry_soil, current_soil, ball_of_string, has_cheese):
	input_needed = True
	print('\nRoom: Attic'+constant.DIVIDER_STR)
	print('You have entered the Attic. There is what seems to be an unlimited supply of cheese up here. How strange you think to yourself. There is also a small hole in the attic floor, too small for any of the cheese to fit through.')
	while input_needed:
		if ball_of_string == 2:
			print(constant.ACTIONS_STR+'\n1) Go down the stairs back to the living room' + '\n2) Try to drop some cheese down the hole'+'\n3) Take some cheese'+'\n4) Drop the ball of string down the hole')
			choice = input(constant.CHOICE_STR)
			choice = input_valid4(choice)
			option4 = True
		else:
			print(constant.ACTIONS_STR+'\n1) Go down the stairs back to the living room' + '\n2) Try to drop some cheese down the hole'+'\n3) Take some cheese')
			choice = input(constant.CHOICE_STR)
			choice = input_valid3(choice)
			option4 = False

		if choice == '1':
			input_needed = False
		elif choice == '2':
			if has_cheese == 0:
				print('Looks like you don\'t have any cheese to drop')
			else:
				print('The cheese is too big to drop down the hole')
			input_needed = True
		elif choice == '3':
			has_cheese += 1
			print('You acquired some cheese.')
			input_needed = True
		elif (choice == '4') and (option4 == True):
			ball_of_string = 0
			print('Heads up down there. You dropped the string down the hole.')
			input_needed = True
	return ball_of_string, has_cheese

# Bedroom


def bedroom(dry_soil, current_soil, ball_of_string, has_cheese):
    input_needed = True
    while input_needed:
        print('\nRoom: Bedroom'+constant.DIVIDER_STR)
        if ball_of_string == 2:
            print('You have entered the Bedroom. Look how comfortable the bed looks. But there\'s no time to take a nap. You notice a black tomcat intently watching a mouse hole.')
            print(constant.ACTIONS_STR + '\n1) Go back to the Living Room' + '\n2) Dangle the string in front of the cat')
            choice = input(constant.CHOICE_STR)
            choice = input_valid2(choice)
            option2 = True
        elif (ball_of_string == 1) or (has_cheese == 0):
            print('You have entered the Bedroom. Look how comfortable the bed looks. But there\'s no time to take a nap. You notice a black tomcat intently watching a mouse hole.')
            print(constant.ACTIONS_STR + '\n1) Go back to the Living Room')
            choice = input(constant.CHOICE_STR)
            choice = input_valid1(choice)
            option2 = False
        else:
            print('You have entered the Bedroom. Look how comfortable the bed looks. But there\'s no time to take a nap. You see a mouse in front of the mouse hole.')
            print(constant.ACTIONS_STR + '\n1) Go back to the Living Room' + '\n2) Give some cheese to the mouse')
            choice = input(constant.CHOICE_STR)
            choice = input_valid2(choice)
            option2 = True

        if choice == '1':
            input_needed = False
        elif (choice == '2') and (option2 == True):
            if ball_of_string == 2:
                print('The cat turns it\'s head towards you. The mouse hole is more important to the cat. It ignores you')
            elif (ball_of_string == 0) and (has_cheese != 0):
                print('Looks like the mouse is a fan of the cheese.')
                current_soil = 'fertilized'
                has_cheese -= 1
            input_needed = True
    return current_soil

# Living Room


def living_room(dry_soil, current_soil, ball_of_string, has_cheese):
    while dry_soil == True:
        input_needed = True
        print('\nRoom: Living Room'+'\n-------------------')
        if ball_of_string == 1:
            print('You have entered the Living Room of the house. The decoration is not to your taste, but neither is having doors dissapear behind you trapping you in a weird house. In the Living Room you see:' + '\n* A pot of soil'+'\n* Stairs going up'+'\n* A dark doorway'+'\n* A ball of string')
            print(constant.ACTIONS_STR + '\n1) View the pot of Soil'+'\n2) Go up the stairs' + '\n3) Go through the dark doorway'+'\n4) Take the ball of string')
            choice = input(constant.CHOICE_STR)
            choice = input_valid4(choice)
            option4 = True
        else:
            print('You have entered the Living Room of the house. The decoration is not to your taste, but neither is having doors dissapear behind you trapping you in a weird house. In the Living Room you see:' + '\n* A pot of soil'+'\n* Stairs going up'+'\n* A dark doorway')
            print(constant.ACTIONS_STR + '\n1) View the pot of Soil' + '\n2) Go up the stairs'+'\n3) Go through the dark doorway')
            choice = input(constant.CHOICE_STR)
            choice = input_valid3(choice)
            option4 = False

        if choice == '1':
            if (current_soil == 'fertilized'):
                dry_soil = False
                print('\nDONE')
            else:
                print('\nThe soil looks dry')
        elif choice == '2':
            ball_of_string, has_cheese = attic(
                dry_soil, current_soil, ball_of_string, has_cheese)
        elif choice == '3':
            current_soil = bedroom(
                dry_soil, current_soil, ball_of_string, has_cheese)
        elif (choice == '4') and (option4 == True):
            ball_of_string = 2
            input_needed = True
    return dry_soil

# Part 1: Entrance, Kitchen, Pantry


def part1():
    door_locked = True
    current_dial = 'blue'
    current_lever = 'forward'

    print('You have just come from outside and into the Entrance Room. The door that you used has just disappeared.')

    door_locked = entryway(door_locked, current_dial, current_lever)

    print('\nCONGRATULATIONS!!!' + '\nYou opened the door. You can now enter the rest of the house.')

# Part 2: Living Room, Attic, Bedroom


def part2():
    dry_soil = True
    current_soil = 'dry'
    ball_of_string = 1
    has_cheese = 0

    print('\nYou turn around and see that the Entrance Room door has also disappeared. It looks like you\'ll be trapped in this house forever. Might as well explore what\'s in it.')

    dry_soil = living_room(dry_soil, current_soil, ball_of_string, has_cheese)

    print('\nIt looks like there is a vine growing from the soil. How did that happen. Oh well, doesn\'t matter now because for some crazy reason you can finally get out of the house' + '... ... ...'+'\nCONGRATULATIONS!!!'+'\nAll that needed to happen was for a vine to somehow magically grow from the soil.')


def main():
    part1()
    part2()


main()
