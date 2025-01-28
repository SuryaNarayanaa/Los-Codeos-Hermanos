nums1 =[1,2,3]
nums2 =[4,5,6]# print(2^1^3^10^2^0)
xor = 0
for i in nums1:
    for j in nums2:
        a= i^j
        xor = xor^a
        print((i,j),xor)
xor = 0
# nums1= list(set(nums1))
# nums2 = list(set(nums2))
def xorAllNums( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1)%2 ==0  and len(nums2)%2==0:
            return 0
        xor = 0
        if len(nums1)%2  and len(nums2)%2:
            for i in nums1:
                xor^=i
            for i in nums2:
                xor^=i
            return xor
            
        if len(nums1)%2 ==0:
            for i in nums1:
                xor^=i
            return xor
        else :
            for i in nums2:
                xor^=i
            return xor

print(xorAllNums(nums1,nums2))