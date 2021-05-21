# CS 362 Homework 1
# By: Jason Graalum
# Run with "Python Jason_Graalum_hw1.py" and enter an integer year when prompted

def leap_year(y):
    if (y % 4 == 0):
        if (y % 100 == 0):
            if (y % 400 == 0):
                print(str(y) + " is a leap year")
            else :
                print(str(y) + " is not a leap year")
        else :
            print(str(y) + " is a leap year")
    else :
        print(str(y) + " is not a leap year")

if __name__ == '__main__':
    y = int(raw_input("Enter the desired year: "))
    leap_year(y)

