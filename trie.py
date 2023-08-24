import re


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_sentence_end = False
        self.sentence_id = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence: str, sentence_id: str):
        """
        Inserts a sentence into the trie
        :param sentence: str input sentence from the user
        :param sentence_id: str a unique id for each sentence
        :return: None
        """
        words = re.sub(r'[^\w\s]+', '', sentence).lower().split()  # remove punctuation marks
        for i in range(len(words)):
            node = self.root
            sliced_phrase = " ".join(words[i:])
            # iterate over each character in the sliced phrase
            for character in sliced_phrase:
                if not node.children.get(character):
                    node.children[character] = TrieNode()
                node = node.children[character]
            # end of the phrase
            node.is_sentence_end = True
            node.sentence_id = sentence_id

    def search(self, prefix: str) -> list[TrieNode]:
        """
        Returns all nodes that starts with prefix, and it represents the word of the sentence
        :param prefix: str input prefix from the user
        :return: list of the nodes that represent the end of sentences
        """

        # find the node that represents the prefix
        node = self.root
        for char in prefix:
            if not node.children.get(char):
                return []
            node = node.children.get(char)

        # find all nodes that represent the end of sentences
        nodes = []
        node_stack = [(node, prefix)]
        while node_stack:
            node, current_key = node_stack.pop()
            if node.is_sentence_end:
                nodes.append(node)
            node_stack.extend((child, current_key + char) for char, child in node.children.items())

        return nodes
