class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = []
        while columnNumber > 0:
            # Adjust for 1-based indexing
            columnNumber -= 1
            # Get the current character
            result.append(chr(columnNumber % 26 + ord('A')))
            # Update columnNumber for the next iteration
            columnNumber //= 26
        # Reverse the result to get the correct order
        return ''.join(reversed(result))