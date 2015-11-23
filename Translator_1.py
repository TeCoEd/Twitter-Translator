from translate import Translator


####TWITTER SECTION###
import os
import time;
import sys, subprocess, urllib, time, tweepy

# == OAuth Authentication ==###############
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'xxxxxxxxxxxxxxx'
consumer_secret= 'xxxxxxxxxxxxxx'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= 'xxxxxxxxxxxxxxx'
access_token_secret= 'xxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

###finding the lanagauge###
print "Welcome to the Twitter Translator"

###CODE TO GET TWITTER TO LISTEN FOR PRAHSE###
class translate_your_tweet(tweepy.StreamListener):
    def on_status(self, tweet):
        
        tweet_to_check = tweet.text ##gets the tweet
        print tweet_to_check
        
        ###Checks for tweets to @PiTests
        does_the_tweet_contain_key_word = tweet_to_check.find("@PiTests")
        ###change to use code to find key word###
        print does_the_tweet_contain_key_word

        ###Finds the space after @PiTests and returns the position
        end_of_key_phrase = tweet_to_check.find(" ")
        print end_of_key_phrase

        ###Returns the phrase to translate to a varibale called final_message_to_translate
        final_message_to_translate = tweet_to_check[end_of_key_phrase:]
        print ("test")
        print final_message_to_translate
        
        if does_the_tweet_contain_key_word == 0:
            try:

                ###converts to string to remove unicode u
                phrase = final_message_to_translate ###phrase to translate
                
                name = tweet.user.screen_name.lower() ###user name of tweeter
                #print ""
                #print name
                #print phrase

                ###Translates English to French
                translator = Translator(to_lang="fr") ###English to French
                translation = translator.translate(phrase) ###translate phrase from twitter

                '''May add the string conversion after this point'''
                translation  =  str(translation)
                #print translation
                #print type(translation)
                
                user = str(tweet.user.screen_name)
                #print type(user)
                
                final_message = "@%s," %(user), translation 
                
                #print final_message
                photo_path = '/home/pi/newpic.jpg'

                #api.update_status(status = final_message)
                api.update_with_media(photo_path, final_message)
                #print ""
                print "Tweet Posted"
                
            
            except:
                 photo_path_error = '/home/pi/error.jpg'
                 print "error"
                 user = str(tweet.user.screen_name)
                 end = str(time.asctime( time.localtime(time.time()) ))
                 error_tweet = "Error, please try another phrase", end
                 print error_tweet
                 error = "@%s" %(user), error_tweet
                 print type(error)
                 api.update_with_media(photo_path_error, error)

                 #api.update_status(status = error)
          
stream = tweepy.Stream(auth, translate_your_tweet())            
            
while True:
    stream.userstream()
    


