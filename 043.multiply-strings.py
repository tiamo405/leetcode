class Solution(object):
    def sum_string(self, num1, num2):
        res = ''
        if len(num1) < len(num2) : 
            tmp = num2
            num2 = num1
            num1 = tmp
        # num1 > num2
        for i in range(len(num1)- len(num2)):
            num2 = '0'+num2
        num1 = num1[::-1]
        num2 = num2[::-1]
        nho = 0
        for i in range(len(num1)):
            tmp = int(num1[i])+ int(num2[i]) + nho
            if tmp >= 10 :
                res += str(tmp-10)
                nho = 1
            else :
                res += str(tmp)
                nho = 0
        if nho == 1 :
            res += '1'
        # print(res[::-1])
        return res[::-1]
    def product_char_string(self, num, a):
        ans = ''
        nho = 0
        num = num[::-1]
        for i in num:
            tmp = int(i) * int(a) + nho
            if tmp >= 10 :
                ans += str(tmp%10)
                nho = tmp // 10
            else :
                ans += str(tmp)
                nho = 0
        if nho > 0:
            ans += str(nho)
        # print(ans[::-1])
        return ans[::-1]

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        result = '0'
        num2 = num2[::-1]
        for i in range(len(num2)) :
            result = self.sum_string(result, self.product_char_string(num1, num2[i])+'0'*i)
        print(result)
        return(result)
a = Solution()
a.multiply('123', '456')
