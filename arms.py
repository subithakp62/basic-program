low = int(input("Enter the lower limit: "))
up = int(input("Enter the upper limit: "))

for i in range(low, up +1):
   pow = len(str(i))
   sum = 0
   temp = i
   while temp > 0:
      digits = temp %10
      sum += digits ** pow
      temp //= 10
   if i == sum:
      print(i)