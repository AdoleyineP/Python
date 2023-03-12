number = input("Please enter the number >> ")
array = [3,6,4,8,5,9,2]
def sortArray(array):
        for num in range(0,len(array)-1):
            min = num
            for nums in range(num + 1, len(array)):
                if array[min] > array[nums]:
                    min = nums
            temp = array[num]
            array[num] = array[min]
            array[min] = temp
def binarySearch(number):
    sortArray(array)
    mid = int(len(array) / 2)
    if number > array[mid]:
         start = a
    
