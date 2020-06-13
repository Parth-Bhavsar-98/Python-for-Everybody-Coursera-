#Write a program to read through the 'Assignment_file_1.txt' and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

x=list()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    word=line.split(" ")
    x=word[1]
    if x in count:
        count[x]=count[x]+1
    else:
        count[x]=1
#print(count)
bigkey = None
bigval = None
for key,val in count.items():
    if val is None or val > bigval:
        bigkey=key
        bigval=val
print(bigkey, bigval)