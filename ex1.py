name = input("Give me your name: ")
age = int(input("How old are you :"))
year = str((2018 - age)+100)
repeat = int(input("How many times?"))
for i in range(repeat):
    print(name + " will be 100 years old in the year " + year)

