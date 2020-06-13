#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#Use file named 'file_for_assignment_2.txt'

count=0
avg=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pp=line.find(" ")
    val=line[pp:].rstrip()
    val=float(val)
    count=count+1
    avg=avg+val
print("Average spam confidence:", avg/count)
