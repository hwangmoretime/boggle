from Board import Board
from Dictionary import Dictionary
import time

from multiprocessing import Pool
from collections import Counter
from operator import add
from functools import partial


def wordcount(dictionary, trials):
    number_of_words = []
    for i in xrange(trials):
        board = Board(dictionary=dictionary)
        number_of_words.append(len(board.words))
    return number_of_words

if __name__ == '__main__':
    processes = 16
    p = Pool(8)
    trials_per_process = 1000

    start = time.time()

    d = Dictionary()
    func = partial(wordcount, d)
    word_counts = reduce(add, p.map(func, [trials_per_process for i in range(processes)]))
    c = Counter(word_counts)

    elapsed_time = time.time() - start
    print c
    print elapsed_time
