Title: Twitter Bots Really Affecting the US Election
Date: 2017-03-23 3:00
Slug: Twitter Bots Really Affecting the US Election
Authors: Matthew Scicluna
Summary: The FBI is investigating allegations that Twitter Bots Really Affected the US Outcome of the US Election. Turns out its very easy to make one!

A [recent story from McClatchy](http://www.mcclatchydc.com/news/politics-government/white-house/article139695453.html) feeds into the continuing narrative that social media programs, better known as "bots," have been deployed by the Russains in an act of subterfuge. These bots have clear political objectives, which they achieve by promoting various news stories/propoganda (depending on if the story aligns with your political preferences.) 

In December, the CIA reported that the Russians were behind the DNC email leaks, and that this was a retaliation for Clintons vocal opposition of Putin. Allegations that Trumps campaign colluded with the Russians have been strengthened by mounting circumstatial evidence. This includes:

- Meetings between Russian officials and high profile members of the Trump campaign staff, including: Michael Flynn, Jeff Sessions, Carter Page, Roger Stone and Paul Manifort.

- Trump and Putins unusually cordial relations despite that the CIA determined that Russia was behind the DNC hack.

We will have to see what comes out of the investigations. In the meanwhile, it is interesting to see how the Russians could very literally manufacture consent. It turns out that you can build your own bot on Twitter, and it doesn't take that much work!

First you want to make a Twitter account. Once you are done you will want to join the dev community for twitter here:
https://dev.twitter.com/resources/signup

Next you want to go to 
https://apps.twitter.com/

hit create new app on the top right corner

add app details. For website and callback URL you can put whatever site you want.

Find your Access level and modify it to include writing permissions (how else are we going to spread propoganda?)

Now we want to get those key and access tokens. This lets our program write stuff on our behalf. Go to "Key and Access token"
Find your Consumer (API key) and Consumer Secret (API secret) keys. copy these into permissions.py dictionary. Generate Access Token and Access Token Secret and copy these into the dict.

To learn more about tweepy go to:
http://docs.tweepy.org/en/v3.5.0/api.html

Don't forget the best practices
https://support.twitter.com/articles/68916
