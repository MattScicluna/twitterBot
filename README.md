<H1>twitterBot</H1>

The bot, as programmed, is just an attention seeker. It fetches tweets using a prespecified hashtag, and then collects the users IDs. It attempts to follow these users. Once it does so, it begins to favorite and retweet some of the users' tweets. It does these in cycles to obey Twitter API limits [1].

There are two options available for what you can do with it. Firstly you can run it as is with minor changes in the conf.py file. This file has a set of parameters you can change to personalize the messages to be sent. The behavior of the bot will remain more or less the same.

Secondly you can modify the source code to make it do whatever you want it to do. The bot makes extensive use of the tweepy Python wrapper around the Twitter API. More information about tweepy can be found [here](http:www.//docs.tweepy.org/en/v3.5.0/api.html).

<h3> Deploying the Bot</h3>
For detailed instructions on how to run the bot, please see my [blog post](https://mattscicluna.github.io/Twitter%20Bots%20Really%20Affecting%20the%20US%20Election.html#.WSwTDnXytOA)


<h3> Running the Bot in the Background</h3>
If you are on Ubuntu, you can deploy this Python script in the background by entering the following into the terminal

```bash
bash backgroundRun.sh 
```

This will execute the Python script using the nohup POSIX command, [which is really great](http:/www./linux.101hacks.com/unix/nohup-command/). You can go to the logs folder to see two files, twitterBot.txt and save_pid.txt. The former is a log of what the bot is up to, and the latter gives out PID information. This PID information You can then kill the process using the following

```bash
kill -KILL PID_NAME
```

where PID_NAME is the PID in save_pid.txt.

<h3> Ethics of Bots</h3>
If you read Twitter's guide for best practices you will notice that Twitter is not a fan of accounts automatically following people. This is what my script does. Why would I post the code of a bot that violates this? The main reason is that everything I did can be easily replicated without reading this article. I am not introducing any new information. I am using open source software, and there are a lot of excellent online reseources on how to use this software. Anyone who wants to deploy a bot on twitter can already do so with nominal programming experience. 

Social engineers and spam artists already have the means to do what they want to do, and have had these means for a while now. You may think that this could inspire new behavior, but I think the news media's constant stream of articles about the far reaching effects of these bots have done far more of that then I could. The main point of this project is only to show that 'Bots' are in fact not very hard to make.

If you want to try out my script out be mindful that your account may be suspended - I only ran it for a couple of iterations. Last of all, there is plenty of room for improvement. This script was written in a couple of hours and has not been tested nearly enough. If anyone wants to propose changes in the source code, feel free to Fork the Github repo, or contact me in the comments or elsewhere.

<br>
<hr>

[1] Twitter API rate limits are detailed [here](https:www.//dev.twitter.com/rest/public/rate-limits)
