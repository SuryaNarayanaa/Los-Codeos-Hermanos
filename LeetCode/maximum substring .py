def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    i,j =0,0
    ss = set()
    ml = 0
    while(i<=j and j<len(s)):
        if s[j] not in ss:
            ss.add(s[j])
            j+=1
        else:
            ss.remove(s[i])
            i += 1
        ml = max(j-i,ml) 
        print(s[i:j])
    return ml
s= "pwwkew"
print(lengthOfLongestSubstring( s))