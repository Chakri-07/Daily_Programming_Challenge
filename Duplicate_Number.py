def duplicate_no(arr):
    fast = arr[0]
    slow = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow
array = list(map(int,input("Enter numbers separated by commas: ").split(',')))
print(duplicate_no(array))