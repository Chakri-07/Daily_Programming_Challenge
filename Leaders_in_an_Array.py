def leaders(arr):
    n = len(arr)
    result = []
    for i in range(0,n):
        if(i==n-1):
            result.append(arr[i])
        else:
            j = 1
            while(arr[i]>arr[i+j]):
                j += 1
                if (i+j == n):
                    result.append(arr[i])
                    break
    return result

arr = list(map(int,input("Enter the array elements seperated by commas: ").split(",")))
Leaders = leaders(arr)
print(Leaders)