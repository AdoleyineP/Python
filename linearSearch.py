number = int(input("Please enter a number your are looking for >> "))
def linearSearch(number):
    listOfNumbers = list(range(0,100))
    for num in listOfNumbers:
        if listOfNumbers[num] == number:
            return "found number"
    return "Number not found"

print(linearSearch(number))