import re

log = "July 31 06:50:25 esa computer bad process  [12345]: ERROR performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
#index = log.index("[")
#print(log[index+1:index+6])
