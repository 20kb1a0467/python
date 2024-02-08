
picnic=list(map(int,input().split()))
size=len(picnic)
capacity=int(input())
count=0
i=0
while(i<size):
    c=picnic[i]
    for j in range(i+1,size):
        c+=picnic[j]
        if c>capacity:
            i=j
            break
    count+=1
    i+=1
print(count)
