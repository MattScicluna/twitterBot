import tweepy, time
import permissions  # Get permissions dictionary


def run(consumer_key, consumer_secret, access_token, access_token_secret):

    # verify credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # log into twitter api
    api = tweepy.API(auth)

    # collect followers
    follower_list = api.followers_ids()

    for follower_id in follower_list:
        list_of_tweets = api.user_timeline(follower_id)  # collect tweets
        for tweet in list_of_tweets:
            try:
                api.create_favorite(tweet.id)  # favorite the tweet
                time.sleep(2)
            except tweepy.TweepError:
                print("already favorited! Moving on...")
            try:
                api.retweet(tweet.id)  # re-tweet the tweet
                time.sleep(2)
            except tweepy.TweepError:
                print("already re-tweeted! Moving on...")


if __name__ == "__main__":
    consumer_key = permissions.PERM_DICT['CONSUMER_KEY']
    consumer_secret = permissions.PERM_DICT['CONSUMER_SECRET']
    access_token = permissions.PERM_DICT['ACCESS_TOKEN']
    access_token_secret = permissions.PERM_DICT['ACCESS_TOKEN_SECRET']

    run(consumer_key, consumer_secret, access_token, access_token_secret)
