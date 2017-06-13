import collections
from collections import defaultdict
import heapq
# import itertools
from datetime import datetime


# class Twitter2(object):

#     def __init__(self):
#         self.timer = itertools.count(step=-1)
#         # {user_id: deque[tweet_id1, tweet_id2, ....]}
#         self.tweets = collections.defaultdict(collections.deque)
#         # {user_id1: set(user_id2, user_id3, ...}
#         self.followees = collections.defaultdict(set)

#     def postTweet(self, userId, tweetId):
#         self.tweets[userId].appendleft((next(self.timer), tweetId))
#
#     def getNewsFeed(self, userId):
#         tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))  # noqa
#         return [t for _, t in itertools.islice(tweets, 10)]
#
#     def follow(self, followerId, followeeId):
#         self.followees[followerId].add(followeeId)
#
#     def unfollow(self, followerId, followeeId):
#         self.followees[followerId].discard(followeeId)


class Tweet(object):

    def __init__(self, message):
        self.message = message
        # self.id = self.create_new_id()
        self.time_stamp = datetime.now().isoformat()
        # creates a chain of tweets
        self.next = None
        self.like_count = 0


class TwitterUser(Tweet):

    def __init__(self, twitter_handle):
        self.twitter_handle = twitter_handle
        self.followees = set()
        # every user has the head of chain for its tweets
        self.tweet_head = None
        # favorited tweets
        self.liked_tweets = []

    def post_tweet(self, tweet_message):
        new_tweet = Tweet(tweet_message)
        new_tweet.next = self.tweet_head
        self.tweet_head = new_tweet

    def follow(self, followee_id):
        self.followees.add(followee_id)

    def unfollow(self, unfollowee_id):
        self.followees.discard(unfollowee_id)

    def __cmp__(self, other):
        return cmp(self.time_stamp, other.time_stamp)

    def get_news_feed(self):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each
        item in the news feed must be posted by users who the user followed or
        by the user herself. Tweets must be ordered from most recent to least
        recent.
        """
        tweets = []
        for user in self.followees:
            # user_obj = self.tweet_map[cur_user]
            tweet_head = user.tweet_head
            while tweet_head is not None:
                tweets.append(tweet_head)
                tweet_head = tweet_head.next
        heapq._heapify_max(tweets)
        return [tweet.message for tweet in tweets[:10]]


class Twitter(TwitterUser):

    def __init__(self):
        """
        Base class for twitter operations.
        """
        # {user_id: [tweet_id1, tweet_id2, ...]}
        self.tweet_map = defaultdict(collections.deque)
        # {user_id: user_object}
        self.user_map = {}

    def add_user(self, twitter_handle):
        new_user = TwitterUser(twitter_handle)
        # Add user as it's own followee so as to get it's tweets in news feed  # noqa
        new_user.followees.add(new_user)
        self.user_map[twitter_handle] = new_user

    def post_tweet(self, twitter_handle, tweet):
        self.user_map[twitter_handle].post_tweet(tweet)

    def get_news_feed(self, twitter_handle):
        return self.user_map[twitter_handle].get_news_feed()

    def follow(self, twitter_handle_followee, twitter_handle_follower):
        self.user_map[twitter_handle_followee].follow(self.user_map[twitter_handle_follower])  # noqa

    def unfollow(self, twitter_handle_followee, twitter_handle_follower):
        self.user_map[twitter_handle_followee].unfollow(self.user_map[twitter_handle_follower])  # noqa

if __name__ == '__main__':
    # test
    twitter_obj = Twitter()
    twitter_obj.add_user('anukul')
    twitter_obj.add_user('steve')
    twitter_obj.post_tweet('anukul', 'Anukul first tweet')
    twitter_obj.post_tweet('anukul', 'Anukul second tweet')
    twitter_obj.post_tweet('anukul', 'Anukul third tweet')
    twitter_obj.post_tweet('steve', 'Steve first tweet')
    twitter_obj.post_tweet('steve', 'Steve second tweet')
    twitter_obj.post_tweet('steve', 'Steve third tweet')
    print 'getting news feed for anukul'
    print twitter_obj.get_news_feed('anukul')
    twitter_obj.follow('anukul', 'steve')
    print 'getting news feed for steve'
    print twitter_obj.get_news_feed('anukul')
    twitter_obj.unfollow('anukul', 'steve')
    print twitter_obj.get_news_feed('anukul')
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
