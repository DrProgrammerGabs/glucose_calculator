"""
        EZ Glucose Calculator for python
        Author: Robert Howell, LPN, NCPT3, HUC
        DATE: 08192015
        version: 0.2
"""

#Menu -----------------------------------------------------------

print("---------Welcome to the pyGlucose Calculator!----------")
print("Press 1 to convert your glucose to an approximate A1C: ")
print("Press 2 to convert your A1C to an average 3mo glucose: ")
print("-------------To exit, hit any other key.---------------")


#variable initialization ----------------------------------------

choice=raw_input(":")
glucose=0
A1C=0

#function definitions -------------------------------------------

def glucose_to_A1C(glucose):
	glucose = int(glucose)
        glucose += 60
	#can't forget to convert total to float
        total = glucose / 30.0
        return total

def A1C_to_glucose(A1C):
	A1C = float(A1C)
        A1C = A1C * 30
        total = A1C - 60
        return total

#Actual Program Engine ------------------------------------------

if choice == "1":
        glucose=raw_input("Enter recent blood sugar:")
        print("Your A1C is approximately: ")
        print glucose_to_A1C(str(glucose))
elif choice == "2":
        A1C=raw_input("Enter A1C result:")
        print("Your average glucose has been approximately: ")
        print A1C_to_glucose(str(A1C))
else:
        print("Thank you!")
        print("Exiting")
