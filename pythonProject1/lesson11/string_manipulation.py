with open('example.txt', 'r')as file:
    for line in file:
        cleaned_file = line.strip()
        print(cleaned_file)


with open("example.txt", "r")as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = "Drin"
age = 17

with open("output.txt", "w")as file:
    file.write("Name: " +name + "\n")
    file.write("Age: " +str(age) + "\n")

with open("output.txt", "w")as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

with open("example.txt", "r") as infile, open("output.txt", "w")as outfile:
    for line in file:
        cleaned_lile= line.strip()
        modified_line = cleaned_lile.replace("Line 1", "Line x")
        outfile.write(modified_line + "\n")