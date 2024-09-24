def atMostKDistinct(s,k):
    count={}
    left=0
    result=0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
        
        while len(count) > k:
            count[s[left]]-=1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
            
        result +=right-left+1
    
    return result

def countSubstringsWithKDistinct(s, k):
    if k==0:
        return 0
    return atMostKDistinct(s, k) - atMostKDistinct(s,k - 1)

print("Please input a string:")
s=input()
k = int(input("Please input an integer k: "))

result = countSubstringsWithKDistinct(s,k)
print(result)