def split(string):
    l = len(string)
    list = []
    for i in range(l):
        list.append(string[i])
    return list

def reverse(chars , ind):
    left = ind
    right = len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return chars


def next_permutation(string):
    chars =  split(string)
    i = len(chars)-2
    j = len(chars) -1
    
    while(i>=0  and  not (chars[i]<chars[i+1])):
        i-=1
    
    while(i>=0 and not (chars[i] < chars[j])):
        j-=1
    
    chars[i] , chars[j] = chars[j], chars[i]
    reverse(chars, i+1)
    return chars

print(next_permutation("23348782394823948"))