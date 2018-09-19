num = int(input("Give me a number: "))
x = list(range(1, num))
divs = []
for element in x:
    if num % element == 0:
        divs.append(element)
print(divs)






