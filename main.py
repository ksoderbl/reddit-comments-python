#!/usr/bin/env python3

import sys
import praw
import time
import math
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show


from secretstuff import client_id, client_secret, user_agent

# do e.g. ./main.py 96nkvw x output.html

def main():
	if len(sys.argv) < 4:
		print('Usage: ./main.py link_id access_token output_file')
		sys.exit()

	#args should be link id, access token and output file name
	linkId = sys.argv[1]
	accessToken = sys.argv[2]
	outputFile = sys.argv[3]

	print("link id is '" + linkId + "'")

	reddit = praw.Reddit(
		client_id=client_id,
		client_secret=client_secret,
#		username=username,
#		password=password,
		user_agent=user_agent)

	submission = reddit.submission(id=linkId)
	print("submission title: " + submission.title)

	commentsCreated = []

	
	i = 1
	submission.comments.replace_more(limit=None)
	for comment in submission.comments.list():
		#print(i, "body	   ", comment.body[0:31])
		#print(i, "author	 ", comment.author)
		#print(i, "permalink  ", comment.permalink)
		#print(i, "created	", comment.created)
		#print(i, "utc		", comment.created_utc)
		commentsCreated.append(comment.created_utc)
		i = i + 1
	
	#print(commentsCreated)

	minTime = min(commentsCreated)
	maxTime = max(commentsCreated)

	diffTime = maxTime - minTime

	print('minTime', minTime)
	print('maxTime', maxTime)
	print('diffTime', diffTime)

	bins = []
	numBins = 100

	for i in range(0, numBins):
		x = minTime + round(i * (diffTime/numBins))
		bins.append(x)


	# --- 2018-08-07
	# https://praw.readthedocs.io/en/latest/tutorials/comments.html
	# Extracting comments with PRAW

	# TODO: to make code understandable, focus on naming
	# and code conventions
	# TODO: testing should be done on the level of unit tests
	# TODO: focus on performance by adding parallelism
	# in comment fetching
	# TODO: for reliable performance, add some retrying
	# logic in case fetching fails
	# TODO: test the program on page
	# https://www.reddit.com/r/videos/comments/88ll08/

	pngFileName = outputFile + '.png'

	fig, ax = plt.subplots(nrows=1, ncols=1)
	#ax.plot([0,1,2], [10,20,3])
	ax.hist(commentsCreated, bins, histtype='bar', rwidth=1.0)
	# save the figure to file
	fig.savefig(pngFileName)
	plt.close(fig)  

	f = open(outputFile, 'w');
	f.write('<!DOCTYPE html>');
	f.write('<html>');
	f.write('<head>');
	f.write('	<meta charset="utf-8">');
	f.write('	<link rel="stylesheet" type="text/css" href="css/style.css">');
	f.write('	<title>Frequency of the comments over time for Reddit link id '+linkId+' </title>');
	f.write('</head>');
	f.write('<body>');
	f.write('	<div class="content">');
	f.write('	<h1>Histogram of comments for Reddit link id '+linkId+'</h1>');
	f.write('	<figure>');
	f.write('		<img src="'+pngFileName+'" width="80%" height="%80" alt="histogram" />');
	f.write('		<figcaption>Frequency of comments for Reddit link id '+linkId+' </figcaption>');
	f.write('	</figure>');
	f.write('</div>');
	f.write('</body>');
	f.write('</html>');
	f.close();

	print("Outputted", outputFile)


if __name__ == '__main__':
	main()
