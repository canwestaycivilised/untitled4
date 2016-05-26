import praw
import time
r=praw.Reddit(user_agent="using my freedom of speech by /u/killbillmaane")
print("yeaaaah boi")
r.login('killbillmaane','hausaufgaben')
words_to_match=['u/']
cache=[]
i=0
def run_bot():
    print("grabbing sub")
    subreddit = r.get_subreddit("redefreiheitkek")
    print("grabbing comments")
    comments=subreddit.get_comments(limit=25)
    for comment in comments:
        comment_text=comment.body.lower()
        isMatch=any(string in comment_text for string in words_to_match)
        if comment.id not in cache and isMatch:
            print("Match found")
            comment.reply("u/autfag u/exit_eu u/Urhorn")
            comment.reply("u/sackg3sicht u/Ede_ u/Fis23")
            comment.reply("u/FranzoseMitRose u/FrischeVollmilch u/geek__")
            print("commented booooi")
            cache.append(comment.id)
    print("loop finished. time to sleep")



while True:
    run_bot()
    time.sleep(600)
