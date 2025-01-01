def split(string):
    l = len(string)
    list = []
    for i in range(l):
        list.append(string[i])
    return list


def permute(ind , chars,  final_arr):
    if(ind == len(chars)):
        final_arr.append(list(chars))
        return
    for i in range(ind ,len(chars)):
        chars[i], chars[ind] = chars[ind] ,chars[i]

        permute(ind+1 ,chars, final_arr)

        chars[ind], chars[i] = chars[i] ,chars[ind]

    return final_arr



l = []
finall= permute(0 , split("10") , l)

for i in range(len(finall)):
    print(i+1, finall[i])