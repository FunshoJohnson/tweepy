import tweepy
# Authenticate to twitter
Auth = tweepy.OAuthHandler("BY01YIQKlfkyiIUSTp79ipiTA", "Qp3bYp3UtckrJFsPtodKCp8igLHUY1gRLVtPo88mHv3dQO8ONw")
Auth.set_access_token("788765954482339840-mQX3qpBNAmnZANLLz7ormsa3uMNAKI9", "N1Ap7qdRD38P1CIBdSTn8E5LkpmIaSW5onFKfMvlJMVtC")
 
api = tweepy.API(Auth)

try:
     api.update_status('i am posting using python')
     print('a tweet is posted')
except:
    print('Error during status')

