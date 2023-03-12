number = int(input("Please enter the number\n>>"))
divisor = 2
remainder = 0
quotient = number
list = []
while(quotient != 0):
    remainder = quotient % divisor
    print(f'{quotient} / {divisor} with remainder {remainder}')
    list.append(remainder)
    quotient = quotient // divisor
print(f'The binary representation of {number} is ',end='')
for num in list:
    print(num,end='')
