#Write a program to read through the 'file_to_use.txt' and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 091416 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

hr = dict()
final = None
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    words=line.split(" ")
    for word in words:
        if ":" in word:
            x=word.split(":")
            y=x[0]
            if y in hr:
                hr[y]=hr[y]+1
            else:
                hr[y]=1
            final=hr.items()
final.sort()
for k,v in final:
    print(k,v)