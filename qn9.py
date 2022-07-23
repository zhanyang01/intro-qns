while True:
    positive_number = int(input("Positive number :"))
    if positive_number > 0 and positive_number < 100:
        break

squ = False
i = 1

while i <= 10:
    square = i**2
    if positive_number == square:
        squ = True
        break
    else:
        squ = False
    i += 1

if positive_number == square:
    print("Perfect square")
else:
    print("Not perfect square")

    

