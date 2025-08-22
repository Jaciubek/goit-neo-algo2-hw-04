from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        # Obsługa błędów wejściowych
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Input must be a list of strings")

        if not strings:  # pusta lista
            return ""

        # Znajdujemy najkrótsze słowo (prefiks nie może być dłuższy od niego)
        shortest = min(strings, key=len)

        prefix = ""
        for i in range(len(shortest)):
            char = shortest[i]
            # Sprawdzamy, czy wszystkie słowa mają ten sam znak na pozycji i
            if all(s[i] == char for s in strings):
                prefix += char
            else:
                break

        return prefix


if __name__ == "__main__":
    # Testy
    try:
        trie = LongestCommonWord()
        strings = ["flower", "flow", "flight"]
        assert trie.find_longest_common_word(strings) == "fl"

        trie = LongestCommonWord()
        strings = ["interspecies", "interstellar", "interstate"]
        assert trie.find_longest_common_word(strings) == "inters"

        trie = LongestCommonWord()
        strings = ["dog", "racecar", "car"]
        assert trie.find_longest_common_word(strings) == ""

        print("All tests completed successfully!")
        
    except AssertionError:
        print("Some tests failed!")