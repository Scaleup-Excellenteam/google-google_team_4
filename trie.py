class TrieNode:
    def __init__(self):
        self.children = {}
        self.filename = ""
        self.is_last = False
        self.sentence_id = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence: str, filename: str, line_number: int, id_to_sentence: dict):
        sentence_id = f"{filename} {line_number}"
        id_to_sentence[sentence_id] = sentence
        words = sentence.split()
        for i in range(len(words)):
            node = self.root
            sliced_phrase = " ".join(words[i:])
            for character in sliced_phrase:
                if not node.children.get(character):
                    node.children[character] = TrieNode()
                node = node.children[character]
            node.is_last = True
            node.filename = filename
            node.sentence_id = sentence_id
