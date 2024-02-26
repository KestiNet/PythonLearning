#!/usr/bin/env python3
import sys
import re
import csv

error_dict = {}
user_dict = {}

info_pattern = r"INFO\s\w+\s\w+\s\[\#\d+\]"
error_pattern = r"ERROR\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\(\w+\)"

def parse_log_entry(entry):
        if re.search(info_pattern, entry):
                username = re.search(r"\((.*?)\)", entry).group(1)
                user_dict[username] = user_dict.get(username, [0, 0])
                user_dict[username][0] += 1
        elif re.search(error_pattern, entry):
                error = re.search(r"ERROR\s(.*?)(\s\(.*?\))?", entry).group(1)
                error_dict[error] = error_dict.get(error, 0) +1

with open('syslog.log', 'r') as file:
        for line in file:
                parse_log_entry(line)

sorted_error = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
sorted_user = sorted(user_dict.items())

sorted_error.insert(0, ("Error", "Count"))
sorted_user.insert(0, ("Username", "INFO", "ERROR"))

with open('error_message.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_error) 

with open('user_statistics.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_user)
