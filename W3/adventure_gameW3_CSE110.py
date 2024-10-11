"""
Hi! I am Agustin Heredia
Activity: W03 Prove: Project Milestone - Adventure Game https://byui-cse.github.io/cse110-ww-course/week03/project.html

For Creativity points, I added multiple unique endings to the game, including a Happy Ending, Dead Ending, Survive Ending, Magic Ending, and Boring Ending, depending on the player's choices throughout the adventure.
"""

# A little introduction
print('Welcome to this Adventure Game!\n')
print("You are escaping from a storm in the middle of the night and you find an abandoned house. You go to the front door and you see that it's slightly open. You have two options: ENTER or LOOK around? \nWhat do you do?")
# First choice
option1 = input()

if option1.lower() == 'enter' : 
    print('You step inside the house. It is dark and you hear a noise upstairs. Do you want to GO UPSTAIRS or HIDE?')
    # Second.1 choice 
    action1 = input()

    if action1.lower() == 'go upstairs' :
        print('You slowly walk upstairs and there is some light coming from the inside of an old chest. You get close to it. Do you OPEN it or LEAVE it?')
        actionChest = input()
        if actionChest.lower() == "open" :
                print("You open the chest and find a treasure! You're rich! \nGame Over | Happy Ending")
        elif actionChest.lower() == "leave" :
                print('You leave the chest untouched. As you turn around, a monster appears! You died.\nGame Over | Dead Ending')
        else:
                print('Wrong choice. You died. \nGameover')

    elif action1.lower() == 'hide' :
        print('You hide behind a curtain. The noise gets louder and louder... \n You see a figure moving the curtain... \n it was just a cat. You survive! \nGame Over | Survive Ending')
    else:
        print('Wrong choice. You died. \nGameover')

elif option1.lower() == 'look' :
    print('You decide to look around the house. Suddenly you find a secret tunnel. Do you want to EXPLORE it or IGNORE it?')
    # Second.2 choice
    action2 = input()

    if action2.lower() == 'explore' :
        print('You enter the tunnel and find yourself in an underground cave with glowing crystals and magical flayers. You discovered a new world! \nGame Over | Magic Ending')
    elif action2.lower() == 'ignore' :
        print("You walk away from the house, but later hear a strange noise behind you. 'Was it a missed opportunity?' you think. Then, after 6hs walking through the storm you get home. \nGame Over | Boring Ending")
    else:
        print('Wrong choice. You died. \nGameover')
else:
    print('Wrong choice. You died. \nGameover')
"""
I hope you enjoyed the game! Come again any time!
"""







