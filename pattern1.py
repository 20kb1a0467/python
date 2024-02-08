n=int(input())
c=input()
for i in range(1,n+1):
    for j in range(1,i):
        print(f"{j}{c}",end="")
        c=chr(ord(c)+1)
    print("\n")
c=chr(ord(c)-n)
for x in range(n-2,0,-1):
    for a in range(0,x):
        print(f"{j}{c}",end="")
        c=chr(ord(c)-1)
    print("\n")
