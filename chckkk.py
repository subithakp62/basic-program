limit=int(input("enter the limit"))
check=int(input("enter the element"))
list=[]
for i in range(limit):
    element=int(input("enter the data"))
    list.append(element)
print("list is..",list)
if check in list:
    print("yes")
else:
    print("no")
