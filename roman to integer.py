def romanToInt( s):
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        count=0
        i=0
        c=0
        while i<len(s)-1:
            if (s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X")) or (s[i]=="X" and (s[i+1]=="C" or  s[i+1]=="L")) or (s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M")):
                   count+=d[s[i+1]]-d[s[i]]
                   c+=2
                   i+=2
            else:
                count+=d[s[i]]
                print(count)
                c+=1
                i+=1
        if c<len(s):
            print(count+d[s[len(s)-1]])
        
        print(count)
s=input()
romanToInt(s)
