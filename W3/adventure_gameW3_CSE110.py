"""
Hi! I am Agustin Heredia
Activity: W03 Prove: Project Milestone - Adventure Game https://byui-cse.github.io/cse110-ww-course/week03/project.html

"""

print('Welcome to this Adventure Game!\n')
print('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
item1 = input(str())

if item1.lower() == 'match' : 
    print('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?')
    action1 = input(str())
        # if  :
#i need to use my creativity here and ad up to 3 questions and responses
        # else:
elif item1.lower() == 'flashlight' :
    print('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?')
    action2 = input(str())

else:
    print('Wrong choice. You died.')
# print(item1)









