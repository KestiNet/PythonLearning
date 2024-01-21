#!/bin/env/python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    print(line.strip())



#!/bin/env/python3

import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    print(line.strip())



import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])



#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    print(result[1])


chmod +x check_cron.py 
./check_cron.py syslog 