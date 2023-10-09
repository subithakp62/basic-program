limit=int(input("enter the limit"))
list1=[]
primelist=[]
notprimelist=[]
for i in range(limit):
    num=int(input("enter the data"))
    list1.append(num)
if (num % i) == 0:
        notprimelist.append(num)
else:
        primelist.append(num)
print("list1")
print(list1)
print("notprimelist")
print(notprimelist)
print("primelist")
print(primelist )
