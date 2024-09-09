def sort(array):
    low = 0
    mid = 0
    high = len(array) - 1

    while mid<=high:
        if array[mid] == 0:
            array[low],array[mid] = array[mid],array[low]
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[high],array[mid] = array[mid],array[high]
            high -= 1
        else:
            print("Invalid Input")
    return array

print("Enter the input array containing only 0,1,2 and was seperated by spaces")
array = list(map(int,input().split))
sortedArray = sort(array)
print("Sorted Array:", sortedArray)