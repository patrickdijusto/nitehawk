import twitter
from settings import *

import urllib2
import re

import time


html_content = urllib2.urlopen('https://nitehawkcinema.com/prospectpark/').read()

matches = re.findall('We look forward to seeing you in Park Slope!', html_content);

if len(matches) > 0: 
   print('No Change')
else:
	## Run entire twitter infrasctucture
	print("Change has come")
	print('establish the twitter object')
	# see "Authentication" section below for tokens and keys
	api = twitter.Api(consumer_key=CONSUMER_KEY,
		consumer_secret=CONSUMER_SECRET,
		access_token_key=OAUTH_TOKEN,
		access_token_secret=OAUTH_SECRET,
	)

	print('twitter object established')
	message = "The Nitehawk Prospect website has changed. But I am only a bot, and I don't know if this means that the theater is open."
	dx = api.PostDirectMessage(text=message,screen_name="@patrickdijusto")
	print(message)
	print(dx)
	time.sleep(30)
	dx = api.PostDirectMessage(text=message,screen_name="@ejgertz")
	print(dx)
	time.sleep(30)
	dx = api.PostDirectMessage(text=message,screen_name="@proggrrl")
	print(dx)
	
	
	
	

	
