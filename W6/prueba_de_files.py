# courses_file = open("demoFiles.txt")   # si uso esto debo cerrarlo al final con  --> courses_file.close() 
# open("C:\Users\Usuario\Desktop\Agu\BYU Pathway Agu\CSE 110 Introduction to Programming\PythonProyects\W6\demoFiles.txt")

with open("demoFiles.txt") as courses_files:
    for line in courses_files: #line puede ser cualquer nombre
        print(line)
    print("Goodbye")
print("The file is closed now.")


line = "     text"

line.strip()

print(line)