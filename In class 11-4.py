
def user_input():

    seq_cont = False
    user_in = ""


def fib(n):

    ans = 0

    if n == 1:
        ans = 0
        return ans
    
    elif n == 2:
        ans = 1
        return ans

    elif n > 2:
        ans = fib(n-1) + fib(n-2)
        return ans



import numpy as np
import random as rd 

array1 = np.ones((5,5))

array2 = np.arange(2,52,2)

array3 = np.full((13, 13), 13)

#####

array4 = np.arange(1, 26, 1)

array4 = array4.reshape(5,5)

array4 = array4.ravel()

#####

array5 = np.random.randn(5,5)



print(array5.size)