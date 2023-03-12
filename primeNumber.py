number = int(input("Please enter a number>> "))
limit  = number // 2
flag = 0
if number == 0 or number == 1:
    print(number, "is not a prime number")
else:
    for numbers in range(2,limit + 1):
        if number % numbers == 0:
            print(number, "is not a prime number")
            flag = 1
    if flag == 0:
        print(number, "is a prime number")
