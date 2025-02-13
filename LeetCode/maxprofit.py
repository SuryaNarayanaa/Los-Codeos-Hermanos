def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        mini = 0
        prof = 0
        for i in range(len(prices)):
            if prices[i] < mini : 
                mini = prices[i]
            if prices[i] - mini > 0 :
                prof = max(prices[i] - mini , prof)

        print(mini , prof)
        return prof

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))