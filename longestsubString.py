def lengthOfLongestSubstring(s):
        char_index=[]
        max_length=0
        left=0
        right=0
        while(right<len(s)):
            if s[right] in char_index and char_index.index(s[right],left,len(s))>=left:
                print(s[right])
                print(*char_index)
                left=char_index.index(s[right],left,len(s))+1
                print(left)
            char_index.append(s[right])
            max_length=max(max_length,right-left+1)
            right+=1
        print(right,left)
        print(*char_index)
        return max_length
      
s=input()
lenght=lengthOfLongestSubstring(s)
print(lenght )
