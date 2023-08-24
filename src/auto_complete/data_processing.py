from pathlib import Path
from trie import Trie

FILE_FORMAT: str = "*.txt"
DIRECTORY_PATH = Path("../../archive")
# DIRECTORY_PATH = Path("")


class DataProcessor:
    def __init__(self):
        self.trie = Trie()
        self.id_to_sentence = {}

    def load_sentences(self):
        for file_path in DIRECTORY_PATH.rglob(FILE_FORMAT):
            self._process_file(file_path)
        return self.trie, self.id_to_sentence

    def _process_file(self, file_path: Path):
        with open(file_path, 'r', encoding="utf-8") as file:
            for line_number, sentence in enumerate(file.readlines()):
                sentence_id = f"{file.name} {line_number}"
                self.id_to_sentence[sentence_id] = sentence
                self.trie.insert(sentence, sentence_id)


def main():
    trie, dic = DataProcessor().load_sentences()
    print(trie.root.children)


if __name__ == '__main__':
    main()