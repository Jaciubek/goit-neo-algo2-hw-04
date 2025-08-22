class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None  # przechowuje wartość przypisaną do słowa (np. indeks)
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key: str, value):
        """Dodaje słowo do drzewa Trie"""
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value

    def get(self, key: str):
        """Zwraca wartość przypisaną do słowa lub None"""
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end else None

    def _collect(self, node, prefix, results):
        """Rekurencyjnie zbiera wszystkie słowa zaczynające się od prefixu"""
        if node.is_end:
            results.append(prefix)
        for char, child in node.children.items():
            self._collect(child, prefix + char, results)

    def keys_with_prefix(self, prefix: str):
        """Zwraca listę wszystkich słów zaczynających się od danego prefixu"""
        results = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return results  # brak dopasowań
            node = node.children[char]
        self._collect(node, prefix, results)
        return results