from functools import lru_cache
### fibonacci Sequence

def fib_seq(n):
    count = 0
    n1,n2 = 0,1
    if n < 0:
        print("Invalid number")
    elif n == 1:
        print(n1)
    else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count+=1


@lru_cache(maxsize=1000)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n-1) + fib(n-2) # fib(4)          +                    fib(3)
                                    # fib(3)            + fib(2)     +   fib(2)  + fib(1)
                                    # fib(2) + fib(1)  + 1           +    1      +  1
                                    #   1    +   1     + 1           +    1      +  1 = 5


def fib2(n):
    n1, n2 = 0,1
    if n < 0:
        return "Invalid number"
    elif n == 1 :
        return n1
    elif n == 2:
        return n1, n2
    else:
        for i in range(n):
            print(n1, end=" ")
            c = n1+n2
            n1 = n2
            n2 = c
fib2(5)



