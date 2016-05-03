# Boggle

This project implements the game Boggle.

To play, run `python main.py`.

Also known as *Scramble with Friends by Zynga*, Boggle is a word game played traditionally with a 4x4 grid of lettered tiles. Players find words in sequences of adjacent letters on the grid.

Play an online versions [here](http://www.wordtwist.org/init4.php).


### Implementation Details
* To get the all the words in a given board, a prefix trie is used to preemptively prune invalid prefixes.
* Heavy use of list comprehensions
