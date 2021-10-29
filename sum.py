import sys
num = int(sys.argv[1])
temp = num
sum = 0
while temp > 0:
    d = temp % 10
    sum = sum + d
    temp = int(temp/10)
print("Sum of digits of entered number = ", sum)
