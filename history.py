import pickle
#cooldowns in days
subreddit_cd = 1
image_cd = 30
combined_cd = 3650

#subreddit history
subreddit = dict()

#image history
image = dict()

#combination history
combined = dict()

def save_history():
    pickle.dump([subreddit, image, combined], open("history.pkl", "wb"))

def load_history():
    try:
        global subreddit
        global image
        global combined
        subreddit, image, combined = pickle.load(open("history.pkl", "rb"))
    except Exception:
        save_history()
