def total_devisors(n):
    m = 2
    for i in range(2,n):
        if n%i==0:
            m+=1
    return m

n = int(input())
print(total_devisors(n))