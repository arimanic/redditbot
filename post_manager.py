import json
from re import template
import praw

class PostManager:

    def __init__(self):
        credentials = 'client_secrets.json'
    
        with open(credentials) as f:
            creds = json.load(f)

        # Uncomment for verbose logging
        # logging.basicConfig()
        # logging.getLogger().setLevel(logging.DEBUG)
        # requests_log = logging.getLogger("requests.packages.urllib3")
        # requests_log.setLevel(logging.DEBUG)
        # requests_log.propagate = True

        self._reddit = praw.Reddit(client_id=creds['client_id'],
                        client_secret=creds['client_secret'],
                        user_agent=creds['user_agent'],
                        redirect_uri=creds['redirect_uri'],
                        refresh_token=creds['refresh_token'],
                        ratelimit_seconds = 600)

        self._reddit.validate_on_submit = True



    def create_post(self, subreddit, template, image): 

        subr = self._reddit.subreddit(subreddit) # Initialize the subreddit to a variable
        # subr = self._reddit.subreddit('pythonsandlot') # TEST

        response = subr.submit_image(template.desc, image, timeout=60, without_websockets=False)
        try:
            response.mod.set_original_content()
        except:
            pass

        # if template.comm:
            # response.reply(template.comm)
        
        return response
