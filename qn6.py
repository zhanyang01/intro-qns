temperature_type = input("C for celsius to fahrenheit/F for fahrenheit to celsius:")
temp = float(input("temperature:"))

if temperature_type == "C":
    if temp > 0 and temp < 100:
        Final = (temp * 1.8) + 32
        print(Final)
    else:
        print("Error as water is no longer in liquid state")

if temperature_type == "F":
    if temp > 32 and temp < 212:
        Final = (temp - 32)/1.8
        print(Final)
    else:
        print("Error as water is no longer in liquid state")    


