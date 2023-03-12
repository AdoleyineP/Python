num1 = 0
num2 = 1
temp = 0

for numbers in range(11):
    temp = num1 + num2
    num1 = num2
    num2 = temp

    print(temp, end = " ")

