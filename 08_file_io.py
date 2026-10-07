# Write data to a file

with open("student.txt", "w") as file:
    file.write("Name: Daniyal\n")
    file.write("Course: Web Development\n")

# Read data from the file

with open("student.txt", "r") as file:
    content = file.read()

print(content)