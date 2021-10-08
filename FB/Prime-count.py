def countPrimes(n):
    if n < 2 :
        return 0

    primes = [True for i in range(n+1)]
    count = 0
    p = 2

    while p*p <= n:
        if primes[p]:
            for i in range(p*2, n+1, p):
                primes[i] = False
        p+=1

    primes[0], primes[1] = False, False

    for i in range(n):
        if primes[i]:
            count +=1

    return count

print(countPrimes(10))

