while True:
    positive_integer = int(input("Positive integer:"))
    if positive_integer > 0:
        break

positive = positive_integer
i = 1
for i in range(8):
    if positive_integer >= 10:
        positive = positive_integer/10
        i += 1
    else:
        print(positive)

        
