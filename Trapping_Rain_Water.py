def Trapped_Water(height):
    left,right = 0,len(height)-1
    Max_From_Left = 0
    Max_From_Right = 0
    Total_Water = 0
    while left<right:
        if height[left]>height[right]:
            if height[right]>=Max_From_Right:
                Max_From_Right = height[right]
            else:
                Total_Water += Max_From_Right - height[right]
            right -= 1
        else:
            if height[left]>=Max_From_Left:
                Max_From_Left = height[left]
            else:
                Total_Water += Max_From_Left - height[left]
            left += 1
    return Total_Water

height = list(map(int,input("Enter the height inputs seperated by commas: ").split(",")))
print(Trapped_Water(height))