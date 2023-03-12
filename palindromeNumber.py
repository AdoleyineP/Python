number = int(input("PLease enter the number>>"))
temp = number
sum = 0
while number > 0:
    reverse = number % 10
    sum = (sum * 10) + reverse
    number = number // 10

number = temp
if sum == temp:
    print(number, "is a Palindrome Number")
else:
    print(number, "is not a Palindrome Number")