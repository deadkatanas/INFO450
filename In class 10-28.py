def GCD(n,m):

    if n == m:
        return n

    else:
        if n<m:
            return GCD(n, m-n)
        else:
            return GCD(n-m, m)

#x=int(input("enter first number "))
#y=int(input("enter second number "))

#print(GCD(x,y))


def string_rev(input1):
    if len(input1) <= 1:
        return input1

    else:
        return input1[-1] + string_rev(input1[0:-1])

xx=input("enter word ")
print(string_rev(xx))