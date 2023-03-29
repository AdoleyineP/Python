number = int(input("Please enter the number >> "))

factorial = number

for num in range(1,number):
    factorial *= number - num

print(f'The factorical of {number} is {factorial}')