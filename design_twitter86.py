"""
Design Twitter (LeetCode #355)

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.

Time Complexity:
- postTweet: O(1)
- getNewsFeed: O(n log k) where n is the number of tweets and k is 10
- follow/unfollow: O(1)

Space Complexity: O(n) where n is the total number of tweets and users
"""

from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeId
        self.timestamp = 0  # Global timestamp for tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Get all tweets from user and their followees
        tweets = []
        # Add user's own tweets
        tweets.extend(self.tweets[userId])
        # Add tweets from followees
        for followeeId in self.following[userId]:
            tweets.extend(self.tweets[followeeId])
        
        # Sort by timestamp in descending order and get top 10
        tweets.sort(reverse=True)
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # Users can't follow themselves
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
