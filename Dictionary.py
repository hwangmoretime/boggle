from Trie import Trie

class Dictionary(object):
	"""docstring for Dictionary"""
	def __init__(self, dictionary_path="./dictionary.txt"):
		super(Dictionary, self).__init__()
		with open(dictionary_path) as f:
			self.words = [word.strip() for word in f]
		self.trie = Trie(self.words)

	def is_prefix(self, prefix):
		return self.trie.in_trie(prefix)

	def is_valid_word(self, prefix):
		return self.trie.is_valid_word(prefix)
