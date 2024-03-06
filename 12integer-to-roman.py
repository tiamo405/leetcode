class Solution(object):
    def demcs(self, num):
        return len(str(num))
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        scs = self.demcs(num)
        for i in range(len(str(num))):
            cs = len(str(num)) - i
            if cs == 4:
                ans = ans + 'M'*int(str(num)[i])
            elif cs ==3:
                if int(str(num)[i])<=3:
                    ans = ans + 'C'*int(str(num)[i])
                elif int(str(num)[i])<5:
                    ans = ans +'C'*(5-int(str(num)[i])) + 'D'
                elif int(str(num)[i])<=8:
                    ans = ans + 'D' + 'C'*(int(str(num)[i])-5)
                else :
                    ans = ans + 'CM'
            elif cs ==2 :
                if int(str(num)[i])<=3:
                    ans = ans + 'X'*int(str(num)[i])
                elif int(str(num)[i])<5:
                    ans = ans +'X'*(5-int(str(num)[i])) + 'L'
                elif int(str(num)[i])<=8:
                    ans = ans + 'L' + 'X'*(int(str(num)[i])-5)
                else :
                    ans = ans + 'XC'
            elif cs ==1 :
                if int(str(num)[i])<=3:
                    ans = ans + 'I'*int(str(num)[i])
                elif int(str(num)[i])<5:
                    ans = ans +'I'*(5-int(str(num)[i])) + 'V'
                elif int(str(num)[i])<=8:
                    ans = ans + 'V' + 'I'*(int(str(num)[i])-5)
                else :
                    ans = ans + 'IX'
        return ans
a= Solution()           
print(a.intToRoman(58))            
