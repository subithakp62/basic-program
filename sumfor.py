num = int(input('Enter a number: '))
sum = 0
for i in range(0, num+1):
    if i % 2 == 0:
        print(i)
        sum+=i

print(f"Sum of all the even numbers is {sum}")