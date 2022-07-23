while True:
    base = int(input("non negative number :"))
    power = int(input("non negative number 2:"))
    if base > 0 and power > 0:
        break

result = base

for i in range(power,1,-1):
    result = result * base
    
print(result)

