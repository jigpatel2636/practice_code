def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(f"{n} is prime number")




numbers = [5,6,7,8,9,10,11,12,13,14,15]
for j in numbers:
    isPrime(j)


res = []
for i in range(10):
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            res.append(i)

print(res)