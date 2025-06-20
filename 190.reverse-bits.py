class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # reverse the bits of n
        result = 0
        n_string = bin(n)[2:]
        n_string = n_string.zfill(32)  # Ensure it is 32 bits
        for i in range(32):
            result = result + int(n_string[i]) * (2 ** i)
        return result
a = Solution()
print(a.reverseBits(0b00000010100101000001111010011100))  # Output: 964176192
print(a.reverseBits(0b11111111111111111111111111111101))  # Output: 3221225471