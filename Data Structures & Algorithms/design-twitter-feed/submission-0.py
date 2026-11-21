from collections import defaultdict
from heapq import nlargest

class Twitter:

    def __init__(self):
        self.user_tweets = defaultdict(list)
        self.user_followings = defaultdict(set)
        self.tweets = defaultdict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        followings = self.user_followings[userId]

        users = set(followings)
        users.add(userId)

        tweets = [self.user_tweets[user][::-1][:10] for user in users]
        tweets = sum(tweets, [])

        return nlargest(10, tweets, key=lambda tweet_id: self.tweets[tweet_id])


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followings = self.user_followings[followerId]

        if followeeId in followings:
            followings.remove(followeeId)
