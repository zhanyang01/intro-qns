num1,num2,num3 = input("Give me 3 integers:").split(",")
num_1 = int(num1)
num_2 = int(num2)
num_3 = int(num3)

largest = num_3

if num_1 > num_2 and num_1 > num_3:
    largest = num_1
elif num_2 > num_1 and num_2 > num_3:
    largest = num_2

print(largest)

