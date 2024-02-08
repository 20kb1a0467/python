def expandFromCentre(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longestPalindrome(s):
    if len(s) < 1:
        return ""
    
    start = 0
    end = 0
    
    for i in range(len(s)):
        len1 = expandFromCentre(s, i, i)
        len2 = expandFromCentre(s, i, i + 1)
        
        length = max(len1, len2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end+1]
def expandFromCentre(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

s = "babagf"
res = longestPalindrome(s)
print(res)
