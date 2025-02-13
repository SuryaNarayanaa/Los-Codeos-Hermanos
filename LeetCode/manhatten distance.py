def maxDistance( s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """

    hset = [0]*4
    for i in s:
        if i == "E":
            hset[0]  +=1
        elif i == "N":
            hset[1]  +=1
        elif i == "S":
            hset[2]  +=1
        else:
            hset[3]  +=1
    while(k):
        maxe , maxv= hset.index(max(hset)) , max(hset)
        while(maxv and k):
            k-=1
            
    # Example call to the function
print(maxDistance("NWSE", 1))