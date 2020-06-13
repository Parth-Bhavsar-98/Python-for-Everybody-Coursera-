#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
#Use the file "file_for_assignment_1.txt" to produce the output below.
fname = input("Enter file name: ")
fh = open(fname)
inp=fh.read()
for i in inp:
    i=i.lstrip()
    final=inp.upper()
print(final)

