n=int(input("enter the number :"))
a=int(input("the first digit to check :"))
while n!=0:
    d=n%10
    n=n//10
if d==a:
    print("start with ",a)
else:
    print("not start with ", a)