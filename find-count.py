#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_209378.txt"
handle = open(name)
fh=handle.read()
stuff=list()
stuff=re.findall('[0-9]+',fh)
x=len(stuff)

y=0
nums=list()


print nums
while x>0:
    nums.append(int(stuff[y]))
    y=y+1
    x=x-1

print sum(nums)