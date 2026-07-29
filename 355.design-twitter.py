class Twitter(object):

    def __init__(self):
        self.post_tweet = {}
        self.followers = {}
        self.time_post = 0
    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time_post += 1
        if userId not in self.post_tweet:
            self.post_tweet[userId] = [[tweetId, self.time_post]]
        else:
            self.post_tweet[userId].append([tweetId, self.time_post])
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        followees = self.followers.get(userId)
        if followees is None:
            followees = set()
        followees.add(userId)
        tweets = []
        for followee in followees:
            if followee in self.post_tweet:
                tweets.extend(self.post_tweet.get(followee))
        tweets.sort(key=lambda x: x[1], reverse=True)
        res = []
        for tweet in tweets:
            res.append(tweet[0])
            if len(res) == 10:
                break
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.followers:
            self.followers[followerId] = set([followeeId])
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.p