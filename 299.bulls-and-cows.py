class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        bulls = 0
        cows = 0
        secret_count = {}
        guess_count = {}
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in secret_count:
                    secret_count[secret[i]] += 1
                else:
                    secret_count[secret[i]] = 1
                if guess[i] in guess_count:
                    guess_count[guess[i]] += 1
                else:
                    guess_count[guess[i]] = 1
        for digit in guess_count:
            if digit in secret_count:
                cows += min(secret_count[digit], guess_count[digit])
        return "{}A{}B".format(bulls, cows)