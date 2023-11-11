# W writes the list items in to the file
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")


new_guests = ["Sam", "Danielle", "Jacob"]

#a Appends text to the file and does not delete it
with open("guests.txt", "a") as guests_file:
    for i in new_guests:
        guests_file.write(i + "\n")

#Iterates through the list and prints the content
with open("guests.txt") as guests:
    for line in guests:
        print(line)

checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests_file:
    for g in guests_file:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests_file:
    for name in temp_list:
        if name not in checked_out:
            guests_file.write(name + "\n")


with open("guests.txt") as guests_file:
    for line in guests_file:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt", "r") as guests_file:
    for g in guests_file:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

