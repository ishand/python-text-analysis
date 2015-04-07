'''Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use raw_input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data.'''
#output
#96.25

# This first line is provided for you
rate = raw_input("Enter Rate:")
rate = float(rate)
hrs = raw_input("Enter Hours:")
hrs = float(hrs)


print rate * hrs

'''2.2 Write a program that uses raw_input to prompt a user for their name and then welcomes them.
 Note that raw_input will pop up a dialog box.
 Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.'''
 #output
 #Hello Sarah
 #The code below almost works

name = raw_input("Enter your name")


print "Hello" +" " + name