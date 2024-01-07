import os
def create_python_scripts(filename):
    comments = "#Start of a new Python program"
    with open("program.py", "w") as file:
        file.write(comments)
        filesize = os.path.getsize("program.py")
    return(filesize)

print(create_python_scripts("program.py"))
