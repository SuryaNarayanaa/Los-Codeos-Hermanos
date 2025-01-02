s = "AAABC"
import collections
freq = dict()
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)
print(collections.Counter(s))