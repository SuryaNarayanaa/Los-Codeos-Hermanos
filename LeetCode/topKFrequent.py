def topKFrequent( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ans  = []
        hashmap = {}
        # Count frequency of each number
        for i in range(len(nums)):
            hashmap[nums[i]] = 1+ hashmap.get(nums[i], 0)
        
        # Sort by frequency in descending order
        s = sorted(hashmap.values() , reverse = True)
        
        # For each of the k highest frequencies
        for i in range(k):
            # Find the number with that frequency
            for key , val in hashmap.items():
                if (s[i] == hashmap[key]):
                    ans.append(key)
                    # Remove the found number from hashmap to avoid duplicates
                    del hashmap[key]
                    break
        return ans


print(topKFrequent([1,2], 2))