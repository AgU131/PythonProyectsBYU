""" 
Hi! I am Agustin Heredia
Project 07: Windchill Project

Creativity points: I added a control in selecting C or F and I also added a function that calculates from fahrenheit to celsius, in order to show both values if celsius is entered.
"""

def wind_chill(temperature, wind): # calculate and return the wind chill value
    temp = temperature
    vel = wind
    wind_chill_value = 35.74 + (0.6215 * temp) - (35.75* (vel ** 0.16)) +(0.4275 * temp * (vel ** 0.16))
    wind_chill_value
    return wind_chill_value

def convert_celsius_fahrenheit (celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

def convert_fahrenheit_celsius (fahrenheit):
    celsius = (fahrenheit - 32) / (9/5)
    return celsius

print('\n******* WIND CHILL CALCULATOR ******\n')

temperature = float(input('What is the temperature? '))

scale = str(input('Fahrenheit or Celsius (F/C)? '))

while scale.lower() != "f" and scale.lower() != "c": # only "C" or "F" allowed
    print("\t please type 'F'' or 'C' ")
    scale = str(input('Fahrenheit or Celsius (F/C)? '))    

if scale.lower() == "f":
    for v in range (5, 61, 5):
        print (f'At temperature {temperature:.1f}°F, and wind speed {v} mph, the windchill is: {wind_chill(temperature, v):.2f}°F')

elif  scale.lower() == "c": # in the case that Celsius is selected, the results is showed in both celsius and fahrenheit
    fahrenheit = convert_celsius_fahrenheit(temperature)
    
    for v in range (5, 61, 5):
        wind_chill_value = wind_chill(fahrenheit, v)
        wind_chill_celsius = convert_fahrenheit_celsius(wind_chill_value)
        print (f'At temperature {temperature:.1f}°C ({fahrenheit:.1f}°F), and wind speed {v} mph, the windchill is:{wind_chill_celsius:.2f}°C ({wind_chill_value:.2f}°F)')