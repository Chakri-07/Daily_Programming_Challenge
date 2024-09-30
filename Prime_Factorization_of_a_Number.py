import math

def prime_factorisation(n):
    factors = []
    while n%2==0:
        factors.append(2)
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            factors.append(i)
            n//=i
    if n>2:
        factors.append(n)
    return factors

n = int(input())
print(prime_factorisation(n))