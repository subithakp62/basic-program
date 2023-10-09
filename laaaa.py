limit=int(input("enter the limit"))
list=[]
for i in range(limit):
    element=int(input("enter the datas"))
    list.append(element)
print("smallest num is:",min(list))