import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "x") as file:
    timestamp = os.path.getctime(filename)
    file_created = datetime.datetime.fromtimestamp(timestamp)
  # Convert the timestamp into a readable format, then into a string
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{:%Y-%m-%d}".format(file_created))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd