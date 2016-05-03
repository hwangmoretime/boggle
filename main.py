from Board import Board
from Dictionary import Dictionary

def main():
	board = Board()
	print board
	print "\n\ntype in p to reprint the board"
	words_found = set()
	while True:
		potential_word = raw_input("Word: ")
		if potential_word == 'p':
			print str(board) + "\n\n"
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


if __name__ == '__main__':
	main()
