import numpy as np

userInput=2

#makes sure input is odd
while userInput%2==0:
    userInput=int(input("enter odd integer: "))

#sets an nxn array, all zero
arr = np.zeros((userInput,userInput))

#def spiral(n):

    #could not figure out the rest... 