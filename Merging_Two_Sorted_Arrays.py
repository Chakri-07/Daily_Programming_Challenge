def merge(arr1, arr2, m, n):
    result = []
    i, j = 0, 0
    
    # Traverse both arrays
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # If there are remaining elements in arr1
    while i < m:
        result.append(arr1[i])
        i += 1
    
    # If there are remaining elements in arr2
    while j < n:
        result.append(arr2[j])
        j += 1
    
    return result

arr1 = list(map(int,input("Enter Sorted array inputs separated by commas: ").split(',')))
arr2 = list(map(int,input("Enter Sorted array inputs separated by commas: ").split(',')))
m = len(arr1) 
n = len(arr2)
merged_array = merge(arr1, arr2, m, n)

def Seperate_Arrays(merged_array,m,n):
    First_Part = merged_array[:m]  # First m elements
    Second_Part = merged_array[m:m+n]  # Remaining n elements
    return First_Part, Second_Part

arr1,arr2 = Seperate_Arrays(merged_array,m,n)
print(f"arr1 = {arr1}")
print(f"arr2 = {arr2}")