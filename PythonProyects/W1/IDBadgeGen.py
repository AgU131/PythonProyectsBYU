"""
Helo helo! This is my code! Ii took a few hours to create it, so please enjoy it.
Activity link: https://byui-cse.github.io/cse110-ww-course/week01/team-activity.html
    Created by Agustin Heredia
"""
#I used '\n' to skip a line (or to create a blank line)
print('Please enter the following information: \n')
#These variables ask for the users information
firstName = input ('What is your Fist Name? ')
lastName = input ('What is your Last Name? ')
emailAddress = input ('What is your Email Address? ')
phoneNumber = input ('What is your Phone Number? ')
jobTitle = input ('What is your Job Title? ')
idNumber = input ('What is your ID Number? ')

# variables that contain the required info
fullName = '{}, {}'.format(lastName.upper(), firstName.capitalize())

# Now we'll be printing all the information received before
print('The ID Card is:')
print('----------------------------------------')
print(fullName)
print(jobTitle.title())
print(f'ID: {idNumber} \n')
print(emailAddress.lower())
print(phoneNumber)
print('----------------------------------------')

"""
This is what I want to recibe                       Example:
                                                
The ID Card is:                                     The ID Card is:
----------------------------------------            ----------------------------------------
[LAST NAME], [first name]                           DOE, Jane
[Job title]                                         Chief Software Architect
ID: [id number]                                     ID: 83-23821

[email address]                                     janedoe@email.com
[phone number]                                      (208) 555-1234
----------------------------------------             ----------------------------------------
"""
#And I did it!!!
