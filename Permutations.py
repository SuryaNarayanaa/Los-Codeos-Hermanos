import itertools
def split(string):
    l = len(string)
    list = []
    for i in range(l):
        list.append(string[i])
    return list

def permutation(chars, permutation_list ,ds, freq):
    if(len(ds) == len(chars)):
        permutation_list.append(list(ds))
        return 
    for i in range( len(chars)):
        if(not freq[i]):
            freq[i] = True
            ds.append(chars[i])
            permutation(chars , permutation_list, ds, freq)
            ds.pop()
            freq[i]= False

    return permutation_list
def find_all_permutation(string):
    chars = split(string=string)
    freq = [False]*len(chars)
    permutation_list = []
    ds = []
    l = permutation(chars, permutation_list ,ds, freq)
    i=1
    for p in l:
        print(i,' '.join(p))
        i+=1

find_all_permutation("ABC$")



