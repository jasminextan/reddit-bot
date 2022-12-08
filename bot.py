import praw
import random
import datetime
import time
import argparse

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "I will never trust the word of [REPUB]. He once told me that he would [DEMACT], but he actually wanted to [REPACT]. I heard he even [HATES] [LOVABLE].",
    "I've heard [REPUB] is kind of wack; he said his deepest desire was to [REPACT]. Even [LOVABLE] [HATE] [REPUB]. I'm [TELLING] you, he's nothing but trouble.",
    "There is no world where [REPUB] is not doing stupid [STUFF] like wanting to [REPACT]. I wish he would [DEMACT], but I guess I would have to vote for Joe Biden. Now there's a man who would never [REPACT].",
    "I like politicans who can stand by [FACTS] like Joe Biden. Politicians like [REPUB] are all just spewing stupid [STUFF] like trying to [REPACT]. I bet if I had [LOVABLE], they would vote for Biden."
    "It's literally gospel that [LOVEABLE] adore Biden. They [HATE] [REPUB] because he tried to [REPACT]. [LOVABLE] are all supporters of the movement to [DEMACT], that's why they vote blue!"
    "I like Biden because my [LOVABLE] [HATE] [REPUB]. I would feel so guilty if they knew I ever voted to [REPACT], and I rather like the movement to [DEMACT], so I guess I'll vote Joe."
]

replacements = {
    'REPUB' : ['Donald Trump', 'Ted Cruz', 'Ron DiSantes', 'Mitch McConnell', 'Mike Pence'],
    'DEMACT' : ['legalize weed', 'create affordable healthcare', 'support gay rights', 'codify gay marriage', 'defund the police', 'codify abortion'],
    'REPACT' : ['strip away abortion rights', 'deny health care', 'deny climate change', 'promote gun rights', 'build a border wall'],
    'HATES' : ['dispises', 'hates', 'loathes', 'detests', 'abhors'],
    'HATE' : ['dispise', 'hate', 'loathe', 'detest', 'abhor'],
    'LOVABLE' : ['babies','dogs','cats','kittens','puppies'],
    'TELLING' : ['telling','warning', 'cautioning','forewarning','alerting'],
    'STUFF' : ['stuff','garbage','nonsense','bunk','gibberish','drivel'],
    'FACTS' : ['facts','statistics','science','data','truth','reality'],
}

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('[' + replacement + ']', random.choice(replacements[replacement]))
    return madlib


# FIXME:
# connect to reddit 
parser = argparse.ArgumentParser()
parser.add_argument('--botnum', default='')
args = parser.parse_args()
bot_name = 'bigjbot' + args.botnum
reddit = praw.Reddit(bot_name, ratelimit_seconds=3600)


# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/zdw9on/jbot_likes_goat_cheese/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    all_comments = []
    print ('replace more start')
    submission.comments.replace_more(limit=None) 
    print ('replace more end')
    all_comments = submission.comments.list()
    
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != bot_name:
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            if len(comment.replies.list()) == 0:
                comments_without_replies.append(comment)
            else:
                has_replied = False
                for reply in comment.replies.list():
                    if reply.author == bot_name:
                        has_replied = True
                if has_replied == False:
                    comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        try:
            rand=random.choice(comments_without_replies)
            rand.reply(generate_comment())
            try:
                highest = 0
                for c in comments_without_replies:
                    if c.score >= highest:
                        highest = c.score
                        to_reply = c 
                to_reply.reply(generate_comment())
                
            except praw.exceptions.APIException:
                print('oops lol deleted')
                pass
        except IndexError:
            print('oops lol this is mine')
            pass

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    next_it = list(reddit.subreddit("cs40_2022fall").hot(limit=5))
    submission=random.choice(next_it)
    
    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(27)