arr = [2,4,3,6,3,0]
sum = 6
# l,h= 0,len(arr)-1
# ans = []
# # while(l<h):
# #     csum=arr[l] +arr[h]
# #     if(csum == sum):
# #         ans.append((arr[l],arr[h]))
# #         l+=1
# #         h-=1
# #     elif(csum<sum):
# #         l+=1
# #     else:
# #         h-=1
# c= set()

# for i in range(len(arr)):
#     complement = sum - arr[i]
#     if(complement in c ):
#         ans.append((arr[i], complement))
#     else:
#         c.add(arr[i])

# print(ans)
ans = []
hashset = dict() # commplement : ind
for i in range(len(arr)):
    complement = sum-arr[i]
    if complement in hashset:
        ans.append((i , hashset[complement]))
    else:
        hashset[arr[i]] = i
print(ans) 