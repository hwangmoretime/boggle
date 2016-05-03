from operator import or_

class TrieNode(object):
	"""docstring for TrieNode"""
	def __init__(self, char, sentinel=False):
		super(TrieNode, self).__init__()
		self.char = char
		self.sentinel = sentinel
		self.children = []

	def __hash__(self):
		return self.char

	def __eq__(self, other):
		return self.char == other

	def add_child(self, treenode):
		self.children.append(treenode)

	def get_child(self, char):
		try:
			return self.children[self.children.index(char)]
		except ValueError:
			return None

	def has_child(self, needle_char):
		return reduce(or_, [child.char == needle_char for child in self.children])

class Trie(object):
	"""docstring for Trie"""
	def __init__(self, words):
		super(Trie, self).__init__()
		self.root = TrieNode(None)

		for word in words:
			current_node = self.root
			for i in range(len(word)):
				char = word[i]
				sentinel = i == len(word) - 1
				child = current_node.get_child(char)
				if not child:
					child = TrieNode(
						char=char,
						sentinel=sentinel
					)
					current_node.add_child(child)
				if sentinel:
					child.sentinel = sentinel
				current_node = child

	def in_trie(self, word):
		trienode = self.get_last_char_trienode(word)
		return bool(trienode)

	def is_valid_word(self, word):
		trienode = self.get_last_char_trienode(word)
		return trienode.sentinel

	def get_last_char_trienode(self, word):
		current_node = self.root
		i = 0
		while i < len(word):
			current_node = current_node.get_child(word[i])
			if not current_node:
				return None
			i += 1
		return current_node if i == len(word) else None


