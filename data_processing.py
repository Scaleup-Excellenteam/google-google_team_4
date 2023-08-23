from pathlib import Path
from trie import Trie

FILE_FORMAT: str = "*.txt"
# DIRECTORY_PATH = Path("archive")
DIRECTORY_PATH = Path("archive_demo")


class DataProcessor:
    def __init__(self):
        self.trie = Trie()

    def process_files(self, id_to_sentence):
        for file_path in DIRECTORY_PATH.rglob(FILE_FORMAT):
            self.process_file(file_path, id_to_sentence)

    def process_file(self, file_path: Path, id_to_sentence):
        with open(file_path, 'r', encoding="utf-8") as file:
            for line_number, sentence in enumerate(file.readlines()):
                self.trie.insert(sentence, file.name, line_number, id_to_sentence)


def main(argv=None):
    id_to_sentence = {}
    data_processor = DataProcessor()
    data_processor.process_files(id_to_sentence)


if __name__ == '__main__':
    main()
