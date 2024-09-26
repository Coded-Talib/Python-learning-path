names = ["John", "Lut", "Salim", "Subaha"]
print(names[3])

i = 1
while i <= 1_0:
    print(i * '*')
    i += 1

weight = int(input('Enter your weight: '))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


temperature = int(input('Enter your temperature: '))

if temperature > 30:
    print("It's a hot a day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

numbers = range(5, 10, 2)
for number in numbers:
    print(number)

numbers = range(5, 10, 2)
for number in numbers:
    print(number)