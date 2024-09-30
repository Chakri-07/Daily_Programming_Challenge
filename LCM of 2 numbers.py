def lcm(m,n):
    gcd = 1
    if m>n:
        for i in range(2,n+1):
            if n%i == 0:
                if m%i == 0:
                    gcd = i
        lcm = (m*n)/gcd
    if n>m:
        for i in range(2,m+1):
            if n%i == 0:
                if m%i == 0:
                    gcd = i
        lcm = (m*n)/gcd
    if m == n:
        lcm = m
    return lcm 
n = int(input())
m = int(input())
print(lcm(m,n))