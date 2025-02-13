def characterReplacement( s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        max_c = 0
        hmap = {}

        while(l<=r and r<len(s)):
                hmap[s[r]] = 1+ hmap.get(s[r], 0) 
                while (r - l + 1 - max(hmap.values()) > k):
                        hmap[s[l]] -=1
                        l+=1
                max_c = max(max_c, r-l+1)
                r += 1
        return max_c
                
            


        
            
s = "AABABBA"
k = 1
result = characterReplacement(s, k)
print(result)  # Output should be 4