limit=int(input("enter the limit"))
l1=[]
for i in range(limit):
    element=int(input("enter the data"))
    l1.append(element)
print(l1)
resultant=[]
for i in l1:
    if i not in resultant:
        resultant.append(i)
print("result after removing duplicates:"+str(resultant))