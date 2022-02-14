# Reddit post bot
import os
import random
import sys
from PIL import Image
import time

from matplotlib.pyplot import hist
import post_template
import image_info
import subreddits
import post_manager as pm
import pickle
import datetime
import history

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
    history.load_history()

    while(True):
        # Check if its a good time to post
        start_time = datetime.datetime.today()
        start_time = start_time.replace(hour=6, minute=30)
        # start_time = datetime.datetime.now()

        if (datetime.datetime.now().hour - start_time.hour) >= 3 or (datetime.datetime.now().hour - start_time.hour) < 0:
            # Calculate time hours to sleep
                
            seconds = (start_time - datetime.datetime.now()).total_seconds()

            if seconds <= 0:
                seconds += 86400

            print(f"slept at {datetime.datetime.now()}")
            time.sleep(seconds)
            # time.sleep(600)
            continue

        # Pull a random image from a folder
        im_name = random.choice(os.listdir("/Applications/Reddit Poster/in_rotation"))
        im_path = os.path.join(os.path.curdir, "in_rotation" , im_name)
        im = Image.open(im_path)

        # Make sure this image has history
        if im_name not in history.image.keys():
            history.image[im_name] = datetime.datetime.min
            history.combined[im_name] = dict()

        # check the last time this was posted
        elapsed = datetime.datetime.now() - history.image[im_name]
        if elapsed.days < history.image_cd:
            continue
        
        # Look up the info needed to fill the template (dimensions, title, comment, wildlife or landscape)
        try:
            info : image_info.ImageInfo = image_info.im_info[im_name]
        except:
            continue

        width = im.width
        height = im.height

        # Find all subreddits that this image can be posted to
        if 'l' in info.category:
            templates = subreddits.landscape_templates
        elif 'w' in info.category:
            templates = subreddits.wildlife_templates
        elif 'p' in info.category:
            templates = subreddits.pic_templates
        elif 'bc' in info.category:
            templates = subreddits.bc_templates
        else:
            templates = {}

        # Get all subreddits. Remove the ones this image has already been posted to
        valid_subreddits = [x for x in templates.keys() if x not in history.combined[im_name].keys()]

        # Remove all subreddits recently posted to
        for subreddit in history.subreddit.keys():
            if subreddit in valid_subreddits and (datetime.datetime.now() - history.subreddit[subreddit]).days < history.subreddit_cd:
                valid_subreddits.remove(subreddit)

        # Choose image again if no valid subreddits for this image
        if len(valid_subreddits) < 1:
            continue

        # Pick a random subreddit
        subreddit = random.choice(valid_subreddits)

        # Check if this image has been posted to this subreddit
        if subreddit in history.combined[im_name].keys():
            if (datetime.datetime.now - history.combined[im_name][subreddit]) < history.combined_cd:
                continue
        
        # Get the template for the randomly selected subreddit
        template : post_template.post_template = templates[subreddit]

        # Fill in the template for that subreddit
        if subreddit == "itookapicture":
            info.title = info.title[0].lower() + info.title[1:]
            template.desc = template.desc.replace('{title}', info.title)
            template.desc = template.desc.replace('{article}', info.article)
        else:
            template.desc = template.desc.replace('{title}', info.title)
        
        try:
            template.desc = template.desc.replace('{width}',  str(im.width))
            template.desc = template.desc.replace('{height}', str(im.height))
        except:
            pass

        #template.comm.format(comment=info.description)

        # create the post
        reference = manager.create_post(subreddit, template, im_path)
        # reference = "abc"
        post_time = datetime.datetime.now()

        # mark the image as posted in that subreddit (probably a pickle table)
        # Add to this image's list of subreddits
        history.combined[im_name][subreddit] = (reference, post_time)
        history.image[im_name] = post_time
        history.subreddit[subreddit] = post_time
        history.save_history()

        print (f"posted {im_name} to {subreddit} at {datetime.datetime.now()}")

        # sleep for a period of time
        time.sleep(600)

if __name__ == "__main__":
    sys.exit(main())
