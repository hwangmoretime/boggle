import random
import string
import math
import operator
from utils import *
from Dictionary import Dictionary

class Board:
    def __init__(self, dictionary=None, dimension=4, min_length_word=3):
        n_tiles = dimension**2
        flattened_board = [random.choice(string.lowercase) for i in range(n_tiles)]

        self.board = [flattened_board[i:i+dimension] for i in range(0, n_tiles, dimension)]
        self.dimension = dimension
        self.min_length_word = min_length_word
        self.words = set()
        self.dictionary = dictionary if dictionary else Dictionary()

        self.get_valid_words()

    def __str__(self):
        uppered_board = []
        for row in self.board:
            uppered_row = [word.upper() for word in row]
            uppered_board.append(uppered_row)

        return "\n".join([" ".join(row) for row in uppered_board])

    def get_valid_words(self):
        for x, y in self.get_all_indices():
            self.get_valid_words_helper(
                current_index=(x, y),
                visited_indexes=set([(x, y)]),
                s=self.board[x][y]
            )

    def get_valid_words_helper(self, current_index, visited_indexes, s):
        adjacent_indices = self.get_adjacent_indices(current_index)
        for index in (adjacent_indices - visited_indexes):
            x, y = index
            next_prefix = s + self.board[x][y]

            if self.is_prefix(next_prefix):
                if self.is_valid_word(next_prefix):
                    self.words.add(next_prefix)

                new_visited_indexes = visited_indexes.copy()
                new_visited_indexes.add(index)
                self.get_valid_words_helper(
                    index,
                    new_visited_indexes,
                    next_prefix,
                )

    def is_in_board(self, word):
        if len(word) == 0:
            return False

        initial_tiles = [(x, y) for x,y in self.get_all_indices() if self.board[x][y] == word[0]]
        for index in initial_tiles:
            in_board = self.is_in_board_helper(
                current_index=index,
                visited_indexes=set([index]),
                s=word[1:]
            )
            if in_board:
                return True
        return False

    def is_in_board_helper(self, current_index, visited_indexes, s):
        if len(s) == 0:
            return True

        adjacent_indices = self.get_adjacent_indices(current_index)
        unvisited_adjacent_indices = (adjacent_indices - visited_indexes)
        if len(unvisited_adjacent_indices) == 0:
            return False

        return reduce_with_default(
            operator=operator.or_,
            iterable=[
                self.is_in_board_helper(
                    current_index=index,
                    visited_indexes=copy_and_add(visited_indexes, index),
                    s=s[1:]
                )
                for index in unvisited_adjacent_indices if self.char_at(index) == s[0]
            ],
            default=False
        )

    def get_adjacent_indices(self, current_index):
        def is_adjacent(current_index, target_index):
            ax, ay = current_index
            bx, by = target_index

            x_delta = abs(ax-bx)
            y_delta = abs(ay-by)

            return ((x_delta == y_delta == 1) or
                    (x_delta == 0 and y_delta == 1) or
                    (x_delta == 1 and y_delta == 0))

        return set([(x, y) for x, y in self.get_all_indices() if is_adjacent(current_index, (x, y))])

    def get_all_indices(self):
        return [(x, y) for x in range(self.dimension) for y in range(self.dimension)]

    def is_prefix(self, prefix):
        return self.dictionary.is_prefix(prefix)

    def is_valid_word(self, word):
        return len(word) >= self.min_length_word and self.dictionary.is_valid_word(word)

    def char_at(self, index):
        x, y = index
        return self.board[x][y]
