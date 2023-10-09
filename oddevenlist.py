limit=int(input("enter the limit"))
list1=[]
evenlist=[]
oddlist=[]
for i in range(limit):
    element=int(input("enter the data"))
    list1.append(element)
    if element % 2==0:
        evenlist.append(element)
    else:
        oddlist.append(element)
print("evenlist")
print(evenlist)
print("oddlist")
print(oddlist)