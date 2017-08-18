from twitter import Twitter, OAuth
import commands

myIP = commands.getoutput("hostname -I")
print(myIP)
tweet = 'Raspberry Pi connected at ' + myIP

token="xxx"
token_secret="yyy"
consumer_key="zzz"
consumer_secret="www"

twitter = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
twitter.statuses.update(status=tweet)
twitter.direct_messages.new(user="mememe", text=tweet)
