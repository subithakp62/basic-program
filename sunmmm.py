a=int(input("enter the limit"))
l1=[]
l2=[]
sumlist=[]
for i in range(0,a):
    element=int(input("enter the data"))
    l1.append(element)
print("first list is:",l1)
for i in range(0,a):
    element=int(input("enter the data"))
    l2.append(element)
print("second list is:",l2)
for i in range(0,len(l1)):
    sumlist.append(l1[i]+l2[i])
print("resultant list is",sumlist)


