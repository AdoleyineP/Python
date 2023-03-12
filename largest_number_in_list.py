list_of_numbers = []

#temp is used to store the current largest number in the list. Which is usually the first number in the list

temp = list_of_numbers[0]

for number in list_of_numbers:
    if number > temp:#if the current number is greater than the number stored in temp then save that number in temp
        temp = number
    else:
        pass
#out the largest value in the list
print("The largest number in the list is", str(temp))