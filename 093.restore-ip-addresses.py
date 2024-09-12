class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        aws = []
        n = len(s)
        def backtrack(start, path):
            if len(path) == 4:
                if sum(path) == n:
                    res.append(path)

                return
            for i in range(start, 4):
                backtrack(1, path+[i])
        backtrack(1, [])
        # return res
        for i in res:
            ip = []
            index = 0
            for j in i:
                ip.append(s[index: index+j])
                index += j
            for inter in ip:
                if int(inter) > 255 or (len(inter) > 1 and inter[0] == '0'):
                    ip = []
                    break
            if ip:
                aws.append('.'.join(ip))
        return aws
a = Solution()
print(a.restoreIpAddresses("101023"))

        