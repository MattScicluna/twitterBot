import tweepy, time, sys, random
from datetime import datetime
import _pickle as pickle
import permissions  # Get permissions dictionary
import conf  # customize text in tweets and DMs sent by program


def get_potential_friends(api):
    potential_friends = []
    for tweet in tweepy.Cursor(api.search, q='#machinelearning').items(30):
        print("added potential friend {}!".format(tweet.author.screen_name))
        potential_friends.append(tweet.author.id)
    return potential_friends


def follow_accounts(api, blacklist):
    potential_friends = get_potential_friends(api)
    actual_added = []
    j = 0
    for potential_friend in potential_friends:
        time.sleep(random.randrange(1, 5))
        if potential_friend not in blacklist and j < conf.ADDS_PER_CYCLE:
            try:
                api.create_friendship(potential_friend)
                actual_added.append(potential_friend)
                print("successfully followed user {}!".format(potential_friend))
                j += 1
            except tweepy.TweepError as e:
                print(e.response)
    return actual_added


def send_dm(api, follower_ids):
    for follower_id in follower_ids:
        try:
            user = api.get_user(follower_id)
            api.send_direct_message(follower_id,
                                    text=conf.generate_dm(user.screen_name))
        except tweepy.TweepError as e:
            print(e.response)

        time.sleep(random.randrange(1, 5))
        print("successfully sent message to user {}!".format(user.screen_name))


def be_nice(api, follower_ids):

    #  how many favorites are left this cycle?
    favs_left = api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining']

    #  distrubute whats left among the new follows:
    if len(follower_ids) > 0:
        limit_favs = max(1, favs_left // len(follower_ids[:conf.FAVS_PER_CYCLE]))
        for follower_id in follower_ids[:conf.FAVS_PER_CYCLE]:
            list_of_tweets = api.user_timeline(follower_id)  # collect tweets
            for tweet in list_of_tweets[:limit_favs]:
                try:
                    api.create_favorite(tweet.id)  # favorite the tweet
                    time.sleep(random.randrange(1, 5))
                    print("successfully favorited tweet {} from user {}"
                          .format(tweet.id, follower_id))
                except tweepy.TweepError as e:
                    print(e.response)
                try:
                    api.retweet(tweet.id)  # re-tweet the tweet
                    time.sleep(random.randrange(1, 5))
                    print("successfully re-tweeted tweet {} from user {}".format(tweet.id, follower_id))
                except tweepy.TweepError as e:
                    print(e.response)
            print("finished being nice to user: {} at time {}"
                  .format(follower_id, time.strftime('%b %d, %H:%M:%S')))
            lim_time = api.rate_limit_status()['resources']['favorites']['/favorites/list']['reset']
            num_rem = api.rate_limit_status()['resources']['favorites']['/favorites/list']['remaining']
            print("remaining favorites: {}"
                  .format(num_rem))
            print("favorites replenish at time: {}"
                  .format(datetime.fromtimestamp(lim_time).strftime('%b %d, %H:%M:%S')))


def run(consumer_key, consumer_secret, access_token, access_token_secret):

    #  initialize lists needed, or load them if previously ran
    try:
        f = open('blacklist.p', 'rb')
        blacklist = pickle.load(f)
        f.close()
        print("Successfully loaded blacklist!")
    except:
        blacklist = []

    try:
        f = open('new_following_list.p', 'rb')
        new_following_list = pickle.load(f)
        f.close()
        print("Successfully loaded list of people I recently followed!")
    except:
        new_following_list = []

    # verify credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # log into twitter api
    api = tweepy.API(auth)

    counter = 0  # Number of iterations to do

    try:
        api.update_status(conf.GOOD_MORNING_MESSAGE)
    except tweepy.TweepError as e:
        print(e.response)

    while counter < conf.NUM_ITER:

        # Begin cycle by sending random messages!
        try:
            api.update_status(random.choice(conf.HELLO_MESSAGE_DICT.keys()))
        except tweepy.TweepError as e:
            print(e.response)

        # follow 10 new accounts, add to running total of new accounts followed
        new_following = follow_accounts(api, blacklist)
        new_following_list.extend(new_following)

        # Get followers list
        followers_list = api.followers_ids()

        # Check if new follows have followed back
        recent_followed_back = list(set(new_following_list).intersection(followers_list))
        still_not_following = list(set(new_following_list) - set(recent_followed_back))

        # If they followed back; send DM and blacklist. We are done with them
        blacklist.extend(recent_followed_back)
        send_dm(api, recent_followed_back)
        new_following_list = list(set(new_following_list) - set(recent_followed_back))

        # If they haven't followed back, be nice!
        #be_nice(api, still_not_following)

        # Remove ones that are not following back after a while
        if len(new_following_list) > conf.MAX_FOLLOW:
            to_remove = new_following_list[:conf.TO_REMOVE]
            blacklist.extend(to_remove)
            for traitor in to_remove:
                try:
                    api.destroy_friendship(traitor)
                    new_following_list.remove(traitor)
                    print("Successfully removed user {}. Did not reciprocate in time".format(traitor))
                except tweepy.TweepError as e:
                    print(e.response)

        #  Wait until next round before next round!
        time_until_next = api.rate_limit_status()['resources']['favorites']['/favorites/list']['reset']
        print("Stopping cycle at time: {} to comply with Twitter rate limits"
              ". Will resume at: {}"
              .format(datetime.now().strftime('%b %d, %H:%M:%S'),
                      datetime.fromtimestamp(time_until_next).strftime('%b %d, %H:%M:%S')))
        #while time.localtime(time_until_next) > time.localtime():
        #    time.sleep(random.randrange(1, 5))

        print("Resuming cycle! Time: {}".format(time.strftime('%b %d, %H:%M:%S')))

        sys.stdout.flush()
        counter += 1

        f = open('new_following_list.p', 'wb')  # 'wb' instead 'w' for binary file
        pickle.dump(new_following_list, f, -1)  # -1 specifies highest binary protocol
        f.close()

        f = open('blacklist.p', 'wb')  # 'wb' instead 'w' for binary file
        pickle.dump(blacklist, f, -1)  # -1 specifies highest binary protocol
        f.close()

        print("Successfully updated blacklist and list of people I recently followed!")


if __name__ == "__main__":
    consumer_key = permissions.PERM_DICT['CONSUMER_KEY']
    consumer_secret = permissions.PERM_DICT['CONSUMER_SECRET']
    access_token = permissions.PERM_DICT['ACCESS_TOKEN']
    access_token_secret = permissions.PERM_DICT['ACCESS_TOKEN_SECRET']

    run(consumer_key, consumer_secret, access_token, access_token_secret)
