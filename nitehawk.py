import twitter
from settings import *

import urllib2
import re

import time

file = open("change.txt","r")
change = file.read()
file.close
print(change)

html_content = urllib2.urlopen('https://nitehawkcinema.com/prospectpark/').read()

matches = re.findall('We look forward to seeing you in Park Slope!', html_content);




if (len(matches) > 0) or (change == "1"): 
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
	time.sleep(5)
	dx = api.PostDirectMessage(text=message,screen_name="@ejgertz")
	print(dx)
	time.sleep(5)
	dx = api.PostDirectMessage(text=message,screen_name="@proggrrl")
	print(dx)
	time.sleep(5)
	dx = api.PostDirectMessage(text=message,screen_name="@tritia")
	print(dx)
	time.sleep(5)
	dx = api.PostDirectMessage(text=message,screen_name="@harrislynn")
	print(dx)
	time.sleep(5)
	dx = api.PostDirectMessage(text=message,screen_name="@saldenaro")
	print(dx)
	time.sleep(5)
	dx = api.PostDirectMessage(text=message,screen_name="@nyisblue")
	print(dx)
	file=open("change.txt","w")
	file.write("1")
	file.close()
