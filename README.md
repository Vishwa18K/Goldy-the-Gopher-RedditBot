# Goldy-the-Gopher-RedditBot
As a current undergraduate at the University of Minnesota Twin Cities, I’ve found Reddit—especially r/uofmn—to be an incredibly helpful resource for navigating university life, academic programs, and more. However, I noticed that the subreddit often contains repeated questions or posts that go unanswered. To help make the online community more effective and supportive, I created this Reddit bot. The bot scans new posts with fewer than five upvotes and replies with useful links to similar discussions or answers, based on the content of the post's title and body. The bot uses the sentence-transformers/all-MiniLM-L6-v2 model from Hugging Face for semantic text matching and the PRAW API to interact with Reddit. All development was done in Google Colab due to local constraints however all code is formatted to work locally (for example used regular praw vs asynchronous praw).

Future plans for the project:

University-Specific Vocabulary: Fine-tune or supplement the model with common University of Minnesota terms (e.g “APAS,” “One Stop,” “East Bank,” course codes) to improve its understanding of context and enhance link matching accuracy.
Feedback Loop: Add a mechanism for users to upvote or downvote bot replies to improve future recommendations.'
