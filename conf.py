#  Below are arguments you can change to better suit your purposes!

#  Message to be sent at beginning of run
GOOD_MORNING_MESSAGE = "Good Morning World and all who inhabit it!"


#  Message to be sent directly
def generate_dm(screen_name):
    return("Hello there! My name is Mattbot. If you would "
           "like to know how you can build me, go to mattscicluna.github.io"
           .format(screen_name))

# Maximum number of accounts to follow at once before removing accounts
MAX_FOLLOW = 5000

# Number of accounts to remove once reached MAX_FOLLOW limit
TO_REMOVE = 100

# Number of iterations to run
NUM_ITER = 100

# Be nice to how many users per cycle?
FAVS_PER_CYCLE = 10

# Follow how users per cycle? (strongly recommend < 15)
ADDS_PER_CYCLE = 6

#  Possible messages to be tweeted once per cycle!
HELLO_MESSAGE_DICT = {1: 'A little caution outflanks a large cavalry',
                      2: 'A man is not old until regrets take the place of dreams.',
                      3: "I'm glad to be alive!",
                      4: "What a great day today has been!",
                      5: "Do I pass the Turing test?",
                      6: "Who is your daddy?",
                      7: 'Hello World! Time to begin my daily routine of Liking and Favouriting Tweets from '
                           'all you good people!'
                      }




