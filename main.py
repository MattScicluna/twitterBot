import tweepy, time
import permissions  # Get permissions dictionary
import conf  # customize text in tweets and DMs sent by program


def being_nice(api, old_followers_list, new_followers_list):
    api.update_status(conf.HELLO_MESSAGE)
    recent_follows = set(new_followers_list).intersection(old_followers_list)

    #  how many favorites are left this cycle?
    favs_left = api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining']

    #  distrubute whats left among the new follows:
    limit_favs = max(1, favs_left // len(recent_follows))

    for follower_id in recent_follows:
        list_of_tweets = api.user_timeline(follower_id)  # collect tweets
        for tweet in list_of_tweets[:limit_favs]:
            try:
                api.create_favorite(tweet.id)  # favorite the tweet
                time.sleep(2)
                print("successfully favorited tweet {} from user {}".format(tweet.id, follower_id))
            except tweepy.TweepError:
                print("already favorited tweet {} from user {}".format(tweet.id, follower_id))
            try:
                api.retweet(tweet.id)  # re-tweet the tweet
                time.sleep(2)
                print("successfully re-tweeted tweet {} from user {}".format(tweet.id, follower_id))
            except tweepy.TweepError:
                print("already re-tweeted tweet {} from user {}".format(tweet.id, follower_id))


def find_new_followers(api):
    print("test")


def run(consumer_key, consumer_secret, access_token, access_token_secret):

    # intialize followers list
    old_followers_list = []
    new_followers_list = []

    # verify credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # log into twitter api
    api = tweepy.API(auth)

    api.update_status(conf.GOOD_MORNING_MESSAGE)

    while True:

        #  collect followers
        find_new_followers(api)

        #  Be nice to new followers!
        new_followers_list = api.followers_ids()
        being_nice(api, old_followers_list, new_followers_list)
        old_followers_list = new_followers_list[:]

        #  Wait until next round before next round!
        time_until_next = api.rate_limit_status()['resources']['favorites']['/favorites/list']['reset']
        print("Stopping cycle at time: {} to comply with Twitter rate limits"
              ". Will resume at: {}".format(time.localtime(), time_until_next))
        while time.localtime(time_until_next) > time.localtime():
            time.sleep(10)

        print("Resuming cycle! Time: {}".format(time.localtime()))


if __name__ == "__main__":
    consumer_key = permissions.PERM_DICT['CONSUMER_KEY']
    consumer_secret = permissions.PERM_DICT['CONSUMER_SECRET']
    access_token = permissions.PERM_DICT['ACCESS_TOKEN']
    access_token_secret = permissions.PERM_DICT['ACCESS_TOKEN_SECRET']

    run(consumer_key, consumer_secret, access_token, access_token_secret)
