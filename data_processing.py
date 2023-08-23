from pathlib import Path
from trie import Trie

FILE_FORMAT: str = "*.txt"
# DIRECTORY_PATH = Path("archive")
DIRECTORY_PATH = Path("archive_demo")


class DataProcessor:
    def __init__(self, id_to_sentence: dict):
        trie = Trie()
        for file_path in DIRECTORY_PATH.rglob(FILE_FORMAT):
            with open(file_path, 'r', encoding="utf-8") as file:
                for line_number, sentence in enumerate(file.readlines()):
                    trie.insert(sentence, file.name, line_number, id_to_sentence)


def main(argv=None):
    id_to_sentence = {}
    data_processor = DataProcessor(id_to_sentence)


if __name__ == '__main__':
    main()
