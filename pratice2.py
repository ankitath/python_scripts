import sys
score = input("Enter Score: ")

try:
    s = float(score)
except:
    print("enter valid input")
    sys.exit(1)
if(s < 0.0 or s > 1.0):
    print("Input out of range")
    sys.exit(1) 

if(s >= 0.9):
    print("A")
elif(s >=0.8):
    print("B")
elif(s >= 0.7):
    print("C")
elif(s >= 0.6):
    print("D")
elif(s < 0.6):
    print("F")


