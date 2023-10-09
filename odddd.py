limit=int(input("enter the limit"))
list=[]
evenlist=[]
oddlist=[]
for i in range(limit):
    element=int(input("enter the data"))
    list.append(element)
    if element % 2==0:
      evenlist.append(element)
    else:
      oddlist.append(element)
print(list)
print("list")
print("evenlist")
print(evenlist)
print("oddlist")
print(oddlist)