'''9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
names = []

for line in handle:
    if not line.startswith('From:'):
        continue
    line = line.rstrip()
    line = line.split()
    names.append(line[1])

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

value_list = counts.values()
max_value = max(value_list)
max_key = max(counts, key = counts.get)
#print max_key,max_value
mostseen = max(counts.values())
for k,v in counts.items():
    if v == mostseen:
        print k, v
#output    
#cwen@iupui.edu 5

'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
 You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
Note that the autograder does not have support for the sorted() function.'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = dict()
c = list()

for line in handle:
    if line.startswith("From "): 
        a = line.split()   
        b = a[5].split(":")
        times[b [0] ]= times.get(b[0],0) + 1
        
lst = list()
for k,v in times.items():
    kval = (k,v)
    lst.append(kval)
    
lst.sort()
for k,v in lst:
    print k,v
#output
'''	
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''