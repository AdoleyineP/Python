array = [1,6,99,56,90,3,9,5,3,8,10,7,2]
print("Before: ", array)
def selectionSort(array):
    for num in range(0,len(array)-1):
        min = num
        for nums in range(1 + num,len(array)):
            if array[min] > array[nums]:
                min = nums
        temp = array[num]
        array[num] = array[min]
        array[min] = temp
    
selectionSort(array)
print("After: ",end="")
for nums in array:
    print(nums, end= " ")