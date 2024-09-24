first_name = input ('What is your first name? ')
last_name = input ('What is your last name? ')
# print(first_name)
# print(last_name)

print('Your name is ' + last_name + ', ' + first_name + ' ' + last_name)

print('Hello ' + first_name.capitalize() + ' ' \
      + last_name.capitalize())


# Formas de programarlo sin los espacios

firstName = 'Agustin'
lastName = 'Heredia'

# output = 'Hello, ' + firstName + ' ' + lastName
# output = 'Hello, {} {}'.format(firstName, lastName)
# output = 'Hello, {0} {1}'.format(firstName, lastName)
    # output = 'Hello, {1}, {0}'.format(firstName, lastName)      #esta es una interesante forma de cambiar el orden de los parametros solo cambiando unos nums
output = f'Hello, {firstName} {lastName}'

print(output)


