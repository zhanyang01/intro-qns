chicken = float(input("Amount of chicken in kg per diner:"))
rice = float(input("Amount of rice in kg per diner:"))
chilli = float(input("Amount of chilli in kg per diner:"))

Diners = int(input("Number of diner:"))

total_chicken = chicken * Diners
total_rice = rice * Diners
total_chilli = chilli * Diners

print(total_chicken)
print(total_rice)
print(total_chilli)