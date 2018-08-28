#!/usr/bin/env python3

import sys
import praw
import time
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def main():

	print("num args:", len(sys.argv))

	if len(sys.argv) < 6:
		print('Usage: python3 main.py link_id client_id client_secret user_agent output_file')
		sys.exit()

	# args should be link id, access token and output file name
	linkId = sys.argv[1]
	client_id = sys.argv[2]
	client_secret = sys.argv[3]
	user_agent = sys.argv[4]
	outputFile = sys.argv[5]
	pngFileName = linkId + '.png'

	print("args:")
	print("link id:", linkId)
	print("client id:", client_id)
	print("client secret:", client_secret)
	print("user_agent:", user_agent)
	print("output file:", outputFile)
	print("output png:", pngFileName)

	# Obtain a submission object
	reddit = praw.Reddit(
		client_id=client_id,
		client_secret=client_secret,
#		username=username,
#		password=password,
		user_agent=user_agent)

	# https://praw.readthedocs.io/en/latest/tutorials/comments.html
	# Comment Extraction and Parsing

	submission = reddit.submission(id=linkId)
	print("submission title: " + submission.title)

	submission.comments.replace_more(limit=None)

	#i = 0
	#top_level_comments = submission.comments
	#for top_level_comment in top_level_comments:
	#	i = i + 1

	#print('Top level comments, i = ', i)
	
	# This list should contain all the comments so we can
	# make a histogram of them.
	commentsCreated = []

	#i = 0
	for comment in submission.comments.list():
		#print(i, "body	   ", comment.body[0:31])
		#print(i, "author	 ", comment.author)
		#print(i, "permalink  ", comment.permalink)
		#print(i, "created	", comment.created)
		#print(i, "utc		", comment.created_utc)
		commentsCreated.append(comment.created_utc)
		#i = i + 1
	
	#print('Total amount of comments, i = ', i)
	n = len(commentsCreated)
	print('Total amount of comments:', n)

	mpl_data = mdates.epoch2num(commentsCreated)
	fig, ax = plt.subplots(nrows=1, ncols=1)
	ax.hist(mpl_data, bins=100, histtype='bar', rwidth=0.8, label="comments", color="k")
	ax.xaxis.set_major_locator(mdates.MonthLocator())
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))
	plt.legend()
	plt.xlabel('Time')
	plt.ylabel('Comments')
	plt.title('Histogram of ' + str(n) + ' comments for reddit link id ' + linkId)
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
	f.write('	<h1>Histogram of comments for Reddit link id '+linkId+'</h1>');
	f.write('	<figure>');
	f.write('		<img src="'+pngFileName+'" width="80%" height="%80" alt="histogram" />');
	f.write('		<figcaption>Frequency of comments for Reddit link id '+linkId+' </figcaption>');
	f.write('	</figure>');
	f.write('</body>');
	f.write('</html>');
	f.close();

	print("Outputted", outputFile)


if __name__ == '__main__':
	main()
