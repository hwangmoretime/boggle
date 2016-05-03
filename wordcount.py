from Board import Board
from Dictionary import Dictionary
from collections import Counter

def wordcount(trials=1000):
	d = Dictionary()
	number_of_words = []
	for i in xrange(trials):
		print "trial {0}".format(i)
		board = Board(dictionary=d)
		number_of_words.append(len(board.words))
	return number_of_words
