from Board import Board
from Dictionary import Dictionary
import time


def main():
	d = Dictionary()
	board = Board(dictionary=d)
	while len(board.words) < 150:
		print len(board.words)
		board = Board(dictionary=d)

	print board
	print "\n\ntype in p to reprint the board"
	words_found = set()

	t_end = time.time() + 60 * 2
	while time.time() < t_end:
		potential_word = raw_input("Word: ")
		if potential_word == 'p':
			print str(board) + "\n\n"
			continue
		if potential_word in words_found:
			print "You already found '{0}'".format(potential_word)
			continue
		if potential_word in board.words:
			words_found.add(potential_word)
			continue
		if not board.is_in_board(potential_word):
			print "{0} is not in the board\n".format(potential_word)
			continue
		if potential_word not in board.words:
			print "{0} is not a word\n".format(potential_word)
			continue
	print "Words found {0}: {1}".format(len(words_found), words_found)
	print "Possible words {0}: {1}".format(len(board.words), board.words)

if __name__ == '__main__':
	main()
