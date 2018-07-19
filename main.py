import sys

def main():
	print(sys.argv)
	print("argv[0]=" + sys.argv[0])

	# TODO: use the reddit api to get comments and their time stamps,
	# find good libraries for using the reddit api
	# https://www.reddit.com/dev/api/
	# TODO: user specifies the input by supplying the link id (not the url),
	# access token and an output file name
	# TODO: calculate a histogram of how many comments appear on the
	# page as function of time
	# TODO: visualize the histogram on an html page
	# TODO: to make code understandable, focus on naming and code conventions
	# TODO: testing should be done on the level of unit tests
	# TODO: focus on performance by adding parallelism in comment fetching
	# TODO: for reliable performance, add some retrying logic in case
	# fetching fails
	# TODO: test the program on page https://www.reddit.com/r/videos/comments/88ll08/
	
if __name__ == '__main__':
	main()
