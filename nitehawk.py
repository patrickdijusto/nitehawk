import twitter
from settings import *
import re

import time

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen







file = open("change.txt","r")
change = file.read()
file.close
print(change)

html_content = urlopen('https://nitehawkcinema.com/prospectpark/').read().decode('utf-8')

matches = re.findall('Nitehawk Cinema Prospect Park is set to open in 2018', html_content);

print(matches)


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
