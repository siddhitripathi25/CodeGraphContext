n=int(input())
a=n%10
c=0
while n>0:
    l=n%10
    n=n//10
    if l!=a:
        c+=1
if c==0:
    print("Yes")
else:
    print("No")
