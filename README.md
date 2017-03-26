Title: Twitter Bots Really Affecting the US Election
Date: 2017-03-23 3:00
Slug: Twitter Bots Really Affecting the US Election
Authors: Matthew Scicluna
Summary: The FBI is investigating allegations that Twitter Bots Really Affected the US Outcome of the US Election. Turns out its very easy to make one!

<style>
img {
   padding:1px;
   border:1px solid #021a40;
   border-radius: 25px;
   margin: 10px;
}
</style>

A [recent story from McClatchy](http://www.mcclatchydc.com/news/politics-government/white-house/article139695453.html) feeds into the continuing narrative that social media programs, better known as "bots," have been deployed by the Russains in an act of subterfuge <sup>[1](#myfootnote1)</sup>. These bots have clear political objectives, which they achieve by promoting various news stories/propoganda (depending on if the story aligns with your political preferences.)

The issue is very complicated. On the one hand, the CIA reported that the Russian government were behind the DNC email leaks, and that this was a retaliation for Clintons vocal opposition of Putin. There are even allegations (with some circumstantial evidence) that Trumps campaign colluded with the Russians! Putin is the guy who lives in the Billion dollar palace despite his salary of $137,000 a year. Journalists who criticize him seem to end up as victims in unsolved murders. He doesn't seem very trustworthy. On the other hand, there are allegations that this is just a Russian witchhunt from people like Glenn Greenwald and John McAfee.

We will have to wait to see what comes out of these investigations. In the meanwhile, it is interesting to see how the Russians *could* very literally manufacture consent. It turns out that you can build your own bot on Twitter, and it doesn't take that much work!

<h3> Starting off</h3>
First you will want the code for the Bot. I wrote some in Python and pushed it into a GitHub repo [here](https://github.com/MattScicluna/twitterBot). You can clone and edit it as you see fit. Next you want to make a Twitter account. Once you do so you will want to join the dev community for twitter [here](https://dev.twitter.com/resources/signup). Go [here](https://apps.twitter.com/) to sign up for a dev account. hit *create new app* on the top right corner (see the picture.)

![Create New App Page](/images/twitterbot/createnewapp.png)

You should see secreen with some fillable text fields. Fill these in however you want. For the website and callback URLs you can put whatever site you want - we won't be using this here. Find your Access level and modify it to include writing permissions (how else are we going to spread propoganda?) When you fill these forms out the next screen should look like the picture below.

![Twitter Dev Page](/images/twitterbot/twitterdevpg.png)

Notice that you can verify the Access Level here. To be able to use my script you will need the Access Level to be at least *Read and Write*. Now we want to get those key and access tokens. This lets our program write stuff on our behalf. Go to the *Key and Access token* tab on the navbar. We are going to need the following things:

- Consumer (API key)
- Consumer Secret (API secret key)
- Access Token 
- Access Token Secret

The consumer key and consumer secret key are easy to find. To get the latter, you will need to generate them. Navigate to the *Token Actions* area and clicking the left button.

![Twitter Dev Page](/images/twitterbot/tokenactions.png)

This in turn will generate the following information.

![Twitter Dev Page](/images/twitterbot/accesstoken.png)

Once you do this you will want to copy this information into the PERM_DICT dictionary in the permissions.py file. The lines you will want to modify should look like:
<br>
{% include_code permissions.py lang:python lines:1-7 %}
<br>

Fill in the corresponding fields. The boring part is now done, and you can start doing some fun stuff<sup>[2](#myfootnote2)</sup>.
 

<h3> The Bot</h3>
The bot, as programmed, is just an attention seeker. It fetches tweets using a prespecified hashtag, and then collects the users IDs. It attempts to follow these users. Once it does so, it begins to favorite and retweet some of the users' tweets. It does these in cycles to obey Twitter API limits <sup>[3](#myfootnote3)</sup>. During each cycle it will perform a check to see if the accounts it is following are following it back, and if so, it will send out a DM (thats Millennialese for "Direct Message".) You can customize that message. For example, if you are a blogger you could reference your blog. If you are working in a web brigade in Moscow you could send some of your favorite Pizzagate articles from InfoWars [(yeah, they actually fell for it.)](http://mashable.com/2017/03/24/infowars-pizzagate-alex-jones-apology/#5w8nDm1gjgqt)

There are two options available for what you can do with it. Firstly you can run it as is with minor changes in the conf.py file. This file has a set of parameters you can change to personalize the messages to be sent. The behavior of the bot will remain more or less the same.

Secondly you can modify the source code to make it do whatever you want it to do. A few notes about this. The bot makes extensive use of the tweepy Python wrapper around the Twitter API. More information about tweepy can be found [here](http://docs.tweepy.org/en/v3.5.0/api.html).

<h3> Running the Bot in the Background</h3>
If you are on Ubuntu, you can deploy this Python script in the background by entering the following into the terminal

```bash
bash backgroundRun.sh 
```

This will execute the Python script using the nohup POSIX command, [which is really great](http://linux.101hacks.com/unix/nohup-command/). You can go to the logs folder to see two files, twitterBot.txt and save_pid.txt. The former is a log of what the bot is up to, and the latter gives out PID information. This PID information You can then kill the process using the following

```bash
kill -KILL PID_NAME
```

where PID_NAME is the PID in save_pid.txt. I recommend reading the best practices [here](https://support.twitter.com/articles/68916). With all this out of the way there is one last thing to mention.

<h3> Ethics of Bots</h3>
If you read Twitter's guide for best practices you will notice that Twitter is not a fan of accounts automatically following people. This is what my script does. Why would I post the code of a bot that violates this? The main reason is that everything I did can be easily replicated without reading this article. I am not introducing any new information. I am using open source software, and there are a lot of excellent online reseources on how to use this software. Anyone who wants to deploy a bot on twitter can already do so with nominal programming experience. 

Social engineers and spam artists already have the means to do what they want to do, and have had these means for a while now. You may think that this could inspire new behavior, but I think the news media's constant stream of articles about the far reaching effects of these bots have done far more of that then I could. The main point of this project is only to show that 'Bots' are in fact not very hard to make.

If you want to try out my script out be mindful that your account may be suspended - I only ran it for a couple of iterations. Last of all, there is plenty of room for improvement. This script was written in a couple of hours and has not been tested nearly enough. If anyone wants to propose changes in the source code, feel free to Fork the Github repo, or contact me in the comments or elsewhere.

<br>
<hr>
<a name="myfootnote1">1</a>: Russains also employed people to act as "bots". These people were also known as "Trolls". It is clear that not all "bots" are "trolls", but notice that, conversly, not all "trolls" are "bots" - a quick visit to 
[4Chan /pol/](http://boards.4chan.org/pol/) will verify this.

<a name="myfootnote2">2</a>: <span style="color:red">Note: By fun I don't mean spreading false news stories</span>.

<a name="myfootnote3">3</a>: Twitter API rate limits are detailed [here](https://dev.twitter.com/rest/public/rate-limits)
