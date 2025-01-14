def reverseVowels( s):
    """
    :type s: str
    :rtype: str
    """
    vow=  "aieou"
    l = 0 
    f1,f2 = 0,0
    r = len(s)-1
    
    while(l<=r):
        if f1 and f2:
            s[f1],s[f2] = s[f2],s[f1]
            f1,f2 = 0,0
            continue

        if (s[l].lower() in vow ):
            f1 =l
            
        if (s[r].lower() in vow ):
            f2 =r
        r-=1
        l+=1
    return s

print(reverseVowels("IceCreAm"))