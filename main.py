# Reddit post bot
import json
from re import template
import praw
import requests
import sys
import logging
from PIL import Image
import os
import time

# Define a post template. It should contain an image, a subject, and a caption. The subject and caption should be auto generated from the image. It may also contain an optional automated comment to plug my gram
class post_template:
    subr = ""
    desc = ""
    comm = ""

    def __init__(self, subreddit, description, comment):
        self.subr = subreddit
        self.desc = description
        self.comm = comment

    def __eq__(self, other: object) -> bool:
        if isinstance(other, post_template):
            return self.subr == other.subr
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.subr)


# Useful title and comment fillers
instagram = "@andrew.rimanic"
title = "Blue and Gold Macaw"
comment = f"A single blue and gold macaw landed in the middle of all of the scarlet macaws. The birds gather on this wall to eat the clay which is rich in minerals that their plant based diets lack. \n\nIG: {instagram}"
country = 'Peru'

# Image info
image_path = '/Users/andrewrimanic/OneDrive/Photos/Reddit/To Post/IMG_3046.jpg'
image = Image.open(image_path)
# Use image.width and image.height for pixel size

# Define a LUT of post templates indexed by subreddit
landscape_templates = {
    # post_template("pythonsandlot", f"{title}", f"{comment}")
    post_template("itookapicture", f"ITAP of {title}", f"{comment}"),
    post_template("nocontextpics", "PIC", f"{comment}"),
    post_template("pics", f"{title}", f"{comment}"),
    post_template("naturepics", f"{title}", f"{comment}"),
    post_template("naturephotography", f"{title}", f"{comment}"),
    post_template("landscapephotography", f"{title} [OC] [{image.width}x{image.height}]", f"{comment}"),
    post_template("casualphoto", f"{title}", f"{comment}"),
    post_template("Images", f"{title}", f"{comment}"),
    post_template("pic", f"{title}", f"{comment}"),
    post_template("travel", f"{title} in {country}", f"{comment}"),
    post_template("campingandhiking", f"{title} in {country}", f"{comment}"),
    post_template("earthporn", f"{title} [OC] [{image.width}x{image.height}] IG:{instagram}", "") # Dont post things with man made objects
}

wildlife_templates = {
    post_template("Natureisfuckinglit", f"\N{fire} {title}", f"{comment}"),
    post_template("itookapicture", f"ITAP of {title}", f"{comment}"),
    post_template("nocontextpics", "PIC", f"{comment}"),
    post_template("pics", f"{title}", f"{comment}"),
    post_template("naturepics", f"{title}", f"{comment}"),
    post_template("naturephotography", f"{title}", f"{comment}"),
    post_template("wildlifephotography", f"{title} [OC] [{image.width}x{image.height}]", f"{comment}"),
    post_template("pic", f"{title}", f"{comment}"),
    post_template("casualphoto", f"{title}", f"{comment}"),
    post_template("Images", f"{title}", f"{comment}")
}




def create_post(template, image, reddit): 

    subr = reddit.subreddit(template.subr) # Initialize the subreddit to a variable

    response = subr.submit_image(template.desc, image, timeout=60, without_websockets=False)

    if template.comm:
        response.reply(template.comm)

def mass_post(templates, image, reddit):
    for template in templates:
        create_post(template, image, reddit)
        time.sleep(300)

def preview_all(templates):
    for template in templates:
        print(f''' Subreddit: {template.subr}
        Title: {template.desc}
        Comment: {template.comm}
        ''')

def main():
    credentials = 'client_secrets.json'
    
    with open(credentials) as f:
        creds = json.load(f)

    # Uncomment for verbose logging
    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True

    reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'],
                     ratelimit_seconds = 600)

    reddit.validate_on_submit = True

    # Remove duplicates
    templates = list(set(wildlife_templates))
    
    # Preview the captions
    preview_all(templates)

    # Confirm that captions are good
    value = input("Are these captions okay? (y/n):\n")
    if(value == 'y'):
        mass_post(templates, image_path, reddit)
        
        # Move the picture to the posted folder
        os.rename(image_path, image_path.replace("To Post", "Posted"))

        print("Image posted")
    else:
        print("Image not posted")

if __name__ == "__main__":
    sys.exit(main())