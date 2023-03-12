listOfNumbers = [1,2,3,4,5,6,7]
while listOfNumbers[0] != 3:
    temp = listOfNumbers[0]
    for numbers in range(0,7):
        
        if numbers < 6:
            listOfNumbers[numbers] = listOfNumbers[numbers + 1]
            print("list index",numbers)
        else:
            listOfNumbers[numbers] = temp  
        
#print(listOfNumbers)
print(listOfNumbers)
print("temp",temp)