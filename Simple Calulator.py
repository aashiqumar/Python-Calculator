# A sample project done Aashiq Umar
# Python Learning Level 1


from json.tool import main
from logging import exception
from re import X
import string
import sys

# Functions
def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Start
print(" \n ~ Simple Python Calculator ~ \n")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division \n")

code = int(input("Enter Code: "))


while True:

# Addition
    if(code == 1):

        print("\n ~ Addition ~\n")
        addNum1 = int(input("\nEnter Num1 : "))
        addNum2 = int(input("Enter Num2 : "))
        print("\n")

        total = addNum1 + addNum2
        print("Total = " + total)

        code1 = input("Do you want to quit? [y/n] : ")

        if(code1 == "y"):
            sys.exit("\n See ya...")

        elif(code1 == "n"):
            print(" \n \n ~ Simple Python Calculator ~ \n")
            print("1. Addition")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division \n")
            code = int(input("Enter Code: "))

# Substraction                
    elif code ==2:

        print("\n ~ Substraction ~\n")
        addNum1 = int(input("\nEnter Num1 : "))
        addNum2 = int(input("Enter Num2 : "))

        print("\n")

        total = addNum1 - addNum2
        print("Total = " + total)

        code1 = input("Do you want to quit? [y/n] : ")

        if(code1 == "y"):
            sys.exit("\n See ya...")

        elif(code1 == "n"):
            print(" \n \n ~ Simple Python Calculator ~ \n")
            print("1. Addition")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division \n")
            code = int(input("Enter Code: "))


# Multiplication
    elif code == 3:

        print("\n ~ Multiplication ~\n")
        addNum1 = int(input("\nEnter Num1 : "))
        addNum2 = int(input("Enter Num2 : "))

        print("\n")

        total = addNum1 * addNum2
        print("Total = " + total)

        code1 = input("Do you want to quit? [y/n] : ")

        if(code1 == "y"):
            sys.exit("\n See ya...")

        elif(code1 == "n"):
            print(" \n \n ~ Simple Python Calculator ~ \n")
            print("1. Addition")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division \n")
            code = int(input("Enter Code: "))

# Dividion
    elif code == 4:

        print("\n ~ Division ~\n")
        addNum1 = int(input("\nEnter Num1 : "))
        addNum2 = int(input("Enter Num2 : "))

        print("\n")

        total = addNum1 / addNum2
        print("Total = " + total)

        code1 = input("Do you want to quit? [y/n] : ")

        if(code1 == "y"):
            sys.exit("\n See ya...")

        elif(code1 == "n"):
            print(" \n \n ~ Simple Python Calculator ~ \n")
            print("1. Addition")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Division \n")
            code = int(input("Enter Code: "))










