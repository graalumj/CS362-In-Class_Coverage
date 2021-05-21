# CS 362 Homework 1
# By: Jason Graalum
# Run with "Python Jason_Graalum_hw1.py" and enter an integer year when prompted
year = (int(input("Please enter year to check: ")))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(str(year) + " is a leap year")
        else :
            print(str(year) + " is not a leap year")
    else :
        print(str(year) + " is a leap year")
else :
    print(str(year) + " is not a leap year")