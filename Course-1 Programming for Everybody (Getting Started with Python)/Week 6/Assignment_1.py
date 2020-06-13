#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not name your variable sum or use the sum() function.

def computepay(h,r):
    if h>40:
        ohr=h-40
        orate=1.5*r
        opay=ohr*orate
        pay=40*r
        tpay=opay+pay
    else:
        tpay=h*r
    return tpay

h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = computepay(h, r)
print("Pay",p)