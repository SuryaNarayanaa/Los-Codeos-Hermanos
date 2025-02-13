def maxDifference(s):
    """
    :type s: str
    :rtype: int
    """
    chars = {}
    for i in s:
        chars[i] = chars.get(i, 0) + 1
    max_odd, min_even = 0, 100
    print(chars)
    for k, v in chars.items():
        if v % 2 == 0 and min_even  > v:
            min_even = v
        if v % 2 != 0 and max_odd < v:
            max_odd = v
    print(max_odd ,min_even)
    return max_odd - min_even

# Example usage
s = "mmsmsym"
result = maxDifference(s)
print("The maximum difference between the most frequent even and odd characters is:", result)
    
