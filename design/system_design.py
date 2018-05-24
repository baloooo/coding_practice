Twitter get home timeline SQL query:

version1: (From github)
SELECT tweet.id, user.username, tweet.message
FROM user
INNER JOIN follow ON user.id = follow.followed_id
INNER JOIN tweet ON tweet.user_id = follow.followed_id
WHERE follow.follower_id = 3

Then, in order to build the home timeline for user 3 (with username Sue), Twitter would only need to run a single SQL query:

Simplification of version 1
select *
From user
Inner join follow on user.user_id = follow.follower_id # Join user and follow to get all users that are followers (DT1)
Inner join tweets on tweets.creator_id = follow.followee_id # Join tweets to derived table (DT1)above to get all tweets created by users that have sue as follower
where follower_id = 3

Alternate version 2
select tweets.tweet_msg
from tweets
where tweets.creator_id in (select follow.followee_id from follow where follow.follower_id = 3)


SELECT tweets.*, users.* FROM tweets
  JOIN users   ON tweets.sender_id    = users.id # Get all the users who have sent any tweets
    JOIN follows ON follows.followee_id = users.id # Join with follow tbl to get users that have followers
      WHERE follows.follower_id = current_user # Filter users who have sue as a follower

