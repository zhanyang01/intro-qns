while True:
    positive_integer = int(input("Positive integer:"))
    if positive_integer > 0:
        break

positive = positive_integer
for i in range(8 ,1,-1):
    if positive >= 10:
        positive = positive_integer//10
        positive_integer = positive   
    else:
        break

print(positive))


        
