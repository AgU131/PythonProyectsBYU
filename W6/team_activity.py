with open("hr_system.txt") as file:
    # The file has now been opened and stored in a variable "f"

    # Read each line, one by one, into a variable: current_line
    for line in file:
        # Split the current line into its parts based on a space " " as the separator
        parts = line.split()   #no necesario poner (" ")      # .strip()

        # Save the parts we need into variables
        name = parts[0]
        title = parts[2]

        # Output the name and title as desired
        print(f"Name: {name}, Title: {title}")

        # {salary:.2f}



""" stretching:
Alexia (ID: 1913), Engineer - $4500.00
Herman (ID: 4266), Manager - $4416.67
Jay (ID: 5849), Engineer - $4875.00
Ahmad (ID: 1326), Tester - $3541.67
Ciaran (ID: 2019), Engineer - $3583.33
Callum (ID: 8005), Engineer - $4041.67
Samantha (ID: 4802), Tester - $3333.33
Antonio (ID: 1423), Tester - $2125.00
May (ID: 5575), CFO - $4666.67
Sebastian (ID: 7378), Scientist - $4250.00
Kaitlyn (ID: 4542), Support - $2625.00
William (ID: 7364), Tester - $3083.33
Sophie (ID: 3437), Engineer - $5541.67
Isaiah (ID: 1518), Designer - $2416.67
Aimee (ID: 8093), CEO - $5208.33
Patrick (ID: 2214), Sales - $3625.00
Gloria (ID: 4414), Designer - $3291.67
Joseph (ID: 9427), Sales - $3791.67
Barbara (ID: 5967), Engineer - $5333.33
"""