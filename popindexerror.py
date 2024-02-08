n = list(map(int, input().split()))
c=[]
for i in range(len(n) - 1, -1, -1):
    if i%2==0:
        print(i)
        c.append(n.pop(i))
        
print(n)
print(c)
