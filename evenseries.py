n=list(map(int,input().split()))
d=[]
n.sort()
for  i in range(0,len(n)) :
       if i%2==0:
           d.append(n[i])
           n.pop(i)
print(*n)
print(*d)
