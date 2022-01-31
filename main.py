# Reddit post bot
import os
import random
import sys
from PIL import Image
import time
import post_template
import image_info
import subreddits
import post_manager as pm
import pickle
import datetime

# Useful title and comment fillers
instagram = "@andrew.rimanic"
title = "Blue and Gold Macaw"
comment = f"A single blue and gold macaw landed in the middle of all of the scarlet macaws. The birds gather on this wall to eat the clay which is rich in minerals that their plant based diets lack. \n\nIG: {instagram}"
country = 'Peru'

# Image info
# image_path = '/Users/andrewrimanic/OneDrive/Photos/Reddit/To Post/IMG_3046.jpg'
# image = Image.open(image_path)
# Use image.width and image.height for pixel size

# Define a LUT of post templates indexed by subreddit


def preview_all(templates):
    for template in templates:
        print(f''' Subreddit: {template.subr}
        Title: {template.desc}
        Comment: {template.comm}
        ''')

def main():
    # Manager for reddit posts
    manager = pm.PostManager()

    # Load history
    try:
        history = pickle.load(open("history.pkl", "rb"))
    except:
        history = dict()

    while(True):
        # Pull a random image from a folder
        im_name = random.choice(os.listdir("/Applications/Reddit Poster/images"))
        im = Image.open(os.path.join(os.path.curdir, "images" , im_name))

        # Make sure this image is in the history
        if im_name not in history.keys():
            history[im_name] = dict()

        # check the last time this was posted
        elapsed = datetime.datetime.now() - history[im_name]["last_posted"]
        if elapsed.days < 7:
            continue
        
        # Look up the info needed to fill the template (dimensions, title, comment, wildlife or landscape)
        info : image_info.ImageInfo = image_info.im_info[im_name]
        width = im.width
        height = im.height

        # Find all subreddits that this image can be posted to
        if info.category == 'l':
            templates = subreddits.landscape_templates
        elif info.category == 'w':
            templates = subreddits.wildlife_templates
        else:
            templates = {}

        # Pick a random subreddit
        valid_subreddits = [x for x in templates.keys() if x not in history[im_name].keys()]
        if len(valid_subreddits) < 1:
            continue

        subreddit = random.choice(valid_subreddits)
        
        # Get the template for the randomly selected subreddit
        template : post_template.post_template = templates[subreddit]

        # Fill in the template for that subreddit
        template.desc.format(title=info.title, width=width, height=height)
        template.comm.format(comment=info.description)

        # create the post
        #reference = manager.create_post(template, im)
        reference = "abc"
        post_time = datetime.datetime.now()

        # mark the image as posted in that subreddit (probably a pickle table)
        # Add to this image's list of subreddits
        history[im_name][subreddit] = (reference, post_time)
        history[im_name]["last_posted"] = post_time
        pickle.dump(history, open("history.pkl", "wb"))

        # sleep for a period of time
        #time.sleep(8*3600)

if __name__ == "__main__":
    sys.exit(main())
