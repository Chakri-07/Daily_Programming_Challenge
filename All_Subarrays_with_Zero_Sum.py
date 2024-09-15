def subarrays(arr):
    result = []
    cumulative_sum = 0
    sum_map = {}
    for i in range(len(arr)):
        cumulative_sum += arr[i]
        if(cumulative_sum == 0):
            result.append((0,i))
        if cumulative_sum in sum_map:
            for index in sum_map[cumulative_sum]:
                result.append((index+1,i))
        if cumulative_sum in sum_map:
            sum_map[cumulative_sum].append(i)
        else:
            sum_map[cumulative_sum] = [i]
    return result
arr = list(map(int,input("Enter the array elements seperated by commas: ").split(",")))
print(subarrays(arr))