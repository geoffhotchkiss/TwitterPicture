#! /usr/bin/env python

import twython
import os
import sys
import getpass

if __name__ == "__main__":
	if len(sys.argv) == 1:
		user = raw_input("Enter your username: ")
	else:
		user = sys.argv[1]
	password = getpass.getpass()
	twitter = twython.core.setup(user, password)
	tweet = raw_input("Enter your tweet: ")
	twitter.updateStatus(tweet);
	os.system("isightcapture picture.jpg")
	twitter.updateProfileImage("picture.jpg")
	os.system("rm picture.jpg")
	print 'All done!'
