# CSCI 040 Project 4: Reddit Bots

## Political Support
My bot is supporting Joe Biden and democratic policies. It opposes Donald Trump, Ted Cruz, Ron Disantis, Mitch McConnell, & Mike Pence.
I must say though, my true feelings about Joe Biden can be summed up with this video:

Bo Burnham - Joe Biden (4K)
[![Bo Burnham - Joe Biden (4K)](https://img.youtube.com/vi/KGmXGkIr7w0/maxresdefault.jpg)](https://www.youtube.com/watch?v=KGmXGkIr7w0)

## Favorite Thread

![My Favorite Thread](https://github.com/jasminextan/reddit-bot/blob/main/reddit%20bot%20screenshot%20thread.png?raw=true)

I like [this](https://old.reddit.com/r/cs40_2022fall/comments/zdw9on/jbot_likes_goat_cheese/izdkh0k/) thread as all of my original 5 bots (0 - 4) are chiming in with their own psycho madlibs about politics. It feels just like thanksgiving dinner, crazy family members ranting about politics at the table :)

Below each comment is a button labeled permalink that lets you link to a comment.

## Bot Summaries
output of bot_counter.py file inside of a markdown code block

I created 5 bots:
[bigjbot](https://old.reddit.com/user/bigjbot/), [bigjbot1](https://old.reddit.com/user/bigjbot1/), [bigjbot2](https://old.reddit.com/user/bigjbot2/), [bigjbot3](https://old.reddit.com/user/bigjbot3/), [bigjbot4](https://old.reddit.com/user/bigjbot4/), [bigjbot5](https://old.reddit.com/user/bigjbot5/), [bigjbot6](https://old.reddit.com/user/bigjbot6/).

Bigjbots 0 - 4 are my original bots I created. Bigjbot5 was made so that I could continue refining my bot.py to try and reach 1000 valid comments without bulldozing over my already somewhat satisfactory score of 939 valid comments on the og bigjbot. Bigjbot6 was made to test my markovify function. 

My markovify function uses a more sophisticated text generating algorithm that uses the `markovify.txt` file that is attached above.  It contains information on [Biden's accomblishments](https://joebiden.com/accomplishments/#), [Trump's history of racism](https://www.vox.com/2016/7/25/12270880/donald-trump-racist-racism-history), and [Biden's economy](https://www.washingtonpost.com/business/bidens-economy-has-the-best-growth-record-since-clinton/2022/08/31/45734024-2925-11ed-a90a-fce4015dfc8f_story.html).

Here are their respective bot_counter outputs:

1. Bot #1: bigjbot
```
bot_name=bigjbot
len(comments)= 1000
len(top_level_comments)= 7
len(replies)= 993
len(valid_top_level_comments)= 3
len(not_self_replies)= 993
len(valid_replies)= 936
========================================
valid_comments= 939
========================================
```

2. Bot #2: bigjbot1
```
```

3. Bot #3: bigjbot2
```
bot_name=bigjbot2
len(comments)= 518
len(top_level_comments)= 5
len(replies)= 513
len(valid_top_level_comments)= 5
len(not_self_replies)= 513
len(valid_replies)= 511
========================================
valid_comments= 516
========================================
```

4. Bot #4: bigjbot3
```
bot_name=bigjbot3
len(comments)= 541
len(top_level_comments)= 5
len(replies)= 536
len(valid_top_level_comments)= 5
len(not_self_replies)= 536
len(valid_replies)= 528
========================================
valid_comments= 533
========================================
```

5. Bot #5: bigjbot4
```
```

6. Bot #6: bigjbot5
```
```

7. Bot #7: bigjbot6
```
```


## My Deserved Score

My final grade should be a resounding (<b>/30</b>)

1. 12 // Completing each of the 6 tasks in bot.py
2. 8 // 936 valid comments (bigjbot)
3. 3 // Github Repo
4. 2 // Responds to highest upvoted comment
5. 2 // Army of 5 bots with 500 valid comments each (bigjbots 0, 1, 2, 3, 4)
6. 2 // Submission bot
7. 5 // Markovify function

Total: 32 (34 w/ submission bot)