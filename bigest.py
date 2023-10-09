def find_large(list):
    large = list[0]
    for a in list:
        if a > large:
            large = a
    return large


num = int(input('How many numbers: '))

lst = []

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("largest Number is :", find_large(lst))
