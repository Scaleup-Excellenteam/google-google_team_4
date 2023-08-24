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
        words = re.sub(r'[^\w\s]+', '', sentence).lower().split()
        for i in range(len(words)):
            node = self.root
            sliced_phrase = " ".join(words[i:])
            for character in sliced_phrase:
                if not node.children.get(character):
                    node.children[character] = TrieNode()
                node = node.children[character]
            node.is_sentence_end = True
            node.sentence_id = sentence_id

    #
    # def get_all_sentences_nodes(self, prefix: str) -> list[TrieNode]:
    #     # returns all nodes that starts with prefix and has is_last = True
    #     nodes = []





