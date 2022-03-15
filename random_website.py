import webbrowser
import random
Site_List = ["https://www.google.com", "https://www.facebook.com", "https://www.youtube.com", "https://www.twitter.com","https://www.w3schools.com"]
choosenWebsite = random.choice(Site_List)
webbrowser.open(choosenWebsite, new=1)

# If new = 0, open URL in same browser window
# If new = 1,  opens URL in new browser window
# If new = 2, open URL in same tab