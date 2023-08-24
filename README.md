# Autocomplete Sentences using Trie

This project involves the implementation of an Autocomplete system for sentences using a Trie data structure. The Trie efficiently stores sentences, allowing users to retrieve sentence suggestions based on a given prefix.
## Algorithms & Structures

- **Trie Data Structure**: The data structure used in this project is a Trie. It's a tree-like structure where each node represents a character in a word. The Trie is constructed by inserting individual words from sentences. Each node contains children nodes for the next characters, and a flag to indicate the end of a sentence. 

## Detailed Code Flow 

The project follows these key steps:
- **TrieNode Class**: Defines the nodes of the Trie. Each node holds references to its children characters, a flag indicating the end of a sentence, and a sentence ID for reference.
- **Trie Class**:  It provides methods to insert sentences into the Trie and retrieve sentence suggestions based on a given prefix.
- **DataProcessor Class**:  Manages the loading of sentences from text files. It processes each file, line by line, assigning a unique sentence ID, and inserting the sentence into the Trie. It also maintains a dictionary to map sentence IDs to their respective sentences.

The project's overall flow includes:

- Initializing the Trie by creating a root TrieNode.
- Loading sentences from text files using the DataProcessor class. Each sentence is assigned a unique sentence ID.
- Constructing the Trie by inserting each sentence into its corresponding nodes.
- The main function showcases the autocomplete functionality. It queries the Trie with a prefix and retrieves sentence suggestions by traversing the Trie nodes.
- The retrieved sentence suggestions are printed to the console.
