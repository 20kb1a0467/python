n=int(input())
alpha={1:"A"}
alphabets={"A":1}
print(alphabets)
i=1
c=2
char=66
while(i<n):
    i=i*c+i
    if i<=n:
        alpha[i]=chr(char)
        alphabets[chr(char)]=i
        char+=1
    c+=1
print(alphabets)
char-=1
str1=""
while(n>0):
    if n-alphabets[chr(char)]<0:
        char-=1
        continue
        
    n=n-alphabets[chr(char)]
    str1+=alpha[alphabets[chr(char)]]
print(str1)
     

    
