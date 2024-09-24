"""
Helo helo! This is my code! I took a few hours to create it, so please enjoy it.
Activity link: https://byui-cse.github.io/cse110-ww-course/week01/project.html
    Created by Agustin Heredia
"""
# I used '\n' to skip a line (or to create a blank line)
print('Please enter the following: \n')
# These variables ask for the users preferences
adjective = input ('adjective: ')
animal = input ('animal: ')
verb1 = input ('verb: ')
exclamation = input ('exclamation: ')
verb2 = input ('verb: ')
verb3 = input ('verb: ')

# variables that contain helps the function look cleaner
exclamationWCaps = exclamation.capitalize()
verb2WNoCaps = verb2.lower()
verb3WNoCaps = verb3.lower()
# An empty print work as '\n'
print()     
print('Your story is: \n')

print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway. "'+ exclamationWCaps +'!" I yelled. But all')
print('I could think to do was to ' + verb2WNoCaps + ' over and over. Miraculously,')
print('that caused it to stop, but not before it tried to ' + verb3WNoCaps)
print('right in front of my family.')




"""
This is what i want to recive:


Please enter the following:

adjective: happy
animal: zebra
verb: sneeze
exclamation: hooray
verb: read
verb: drive

Your story is:

The other day, I was really in trouble. It all started when I saw a very
happy zebra sneeze down the hallway. "Hooray!" I yelled. But all
I could think to do was to read over and over. Miraculously,
that caused it to stop, but not before it tried to drive
right in front of my family.

"""
#And i did it!!!!