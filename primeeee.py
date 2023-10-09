a=[]
n=int(input("enter the limit"))
print("enter the elements:")
for i in range(0,n):
    k=int(input("enter the elements"))
    a.append(k)
print("prime numbers are:")
for i in range(0,n):
    if a[i]==1:
        continue
    for j in range(2,a[i]):
        if a[i]%j==0:
            break
    else:
        print(list[i])
