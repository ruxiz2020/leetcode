import heapq


class User(object):
    """
    User structure
    """
    def __init__(self, userId):
        self.userId = userId
        self.tweets = set()
        self.following = set()

class Tweet(object):
    """
    Tweet structure
    """
    def __init__(self, tweetId, userId, ts):
        self.tweetId = tweetId
        self.userId = userId
        self.ts = ts

    def __cmp__(self, other):
        #call global(builtin) function cmp for int
        return cmp(other.ts, self.ts)

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = 0
        self.userMap = dict() # hash set


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.userMap:
            self.userMap[userId] = User(userId)
        tweet = Tweet(tweetId, userId, self.ts)
        self.userMap[userId].tweets.add(tweet)
        self.ts += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = list()
        que = []
        if userId not in self.userMap:
            return res
        mainUser = self.userMap[userId]
        for t in mainUser.tweets:
            heapq.heappush(que, t)
            heapq.heappush(que, t)
        for u in mainUser.following:
            for t in u.tweets:
                heapq.heappush(que, t)
        n = 0
        while que and n < 10:
            res.append(heapq.heappop(que).tweetId)
            n += 1
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId not in self.userMap:
            self.userMap[followeeId] = User(followeeId)
        if followerId not in self.userMap:
            self.userMap[followerId] = User(followerId)
        if followerId == followeeId:
            return
        followee = self.userMap[followeeId]
        self.userMap[followerId].following.add(followee)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if (followerId == followeeId) or (followerId not in self.userMap) or (followeeId not in self.userMap):
            return
        followee = self.userMap[followeeId]
        if followee in self.userMap.get(followerId).following:
            self.userMap.get(followerId).following.remove(followee)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
