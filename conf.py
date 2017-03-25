#  Below are arguments you can change to better suit your purposes!

#  Message to be tweeted prior to doing friendly action!
HELLO_MESSAGE = "Hello World! Time to begin my daily routine of Liking and Favouriting Tweets from all you good people!"

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
NUM_ITER = 24