def reverseWords( s):
    """
    :type s: str
    :rtype: str
    """
    def reverse(s,l,r):
        while(l<r):
            s[l],s[r]= s[r],s[l]
            l+=1
            r-=1
        return s

    s =list(reversed(s))
    i=0
    start,end =0 ,0
    while(i<len(s)):
        while i < len(s) and s[i] == ' ' :
            s.pop(i)
        while( i<len(s) and s[i]!= ' '):
            i+=1
        if(i==len(s)):
            s = reverse(s,start,i-1)
            break
        s = reverse(s,start,i-1)
        
        i+=1
        start =i

    while s and s[-1] == ' ':
        s.pop()

    return ''.join(s)
print(reverseWords("Let's take LeetCode contest"))