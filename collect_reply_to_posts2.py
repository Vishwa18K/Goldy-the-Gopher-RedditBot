# AUTH#
import praw
import csv
import string
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="<Windows>:<>:<7.8.1> (by u/<>)",
    username="",
)












# raw_weekly_posts = []
# weekly_posts = []

# weekly_posts.clear()

# for submission in reddit.subreddit("uofmn").new(limit=None):
   

#     clean_title = ''.join([c for c in submission.title if c in string.printable])
#     clean_selftext = ''.join([c for c in submission.selftext if c in string.printable])

#     combined_line = f"{clean_title}: {clean_selftext}"
#     weekly_posts.append(combined_line)


# file = open("weekly_posts.csv", "w", newline="", encoding="utf-8")
# writer = csv.writer(file) 
# writer.writerow(["Titles"])  
# for line in weekly_posts:
#     writer.writerow([line])
# file.close()

for submission in reddit.subreddit("uofmn").search("undergrad graduation + google workspace access"):
        if submission.title.lower() == "undergrad graduation + google workspace access":
            submission.reply("Here are some submission titles that have similar names:\n How much longer do we get RecWell access?,\n GMAIL REMOVAL IS FINAL,\nEmail expiring after 8 years:,\nDid Anyone Else's University Google Drive Storage Just Shrink?\n")