def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            print(L)
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
        

convert("PAYPALISHIRING", 3)