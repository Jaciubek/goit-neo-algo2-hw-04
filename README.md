# goit-neo-algo2-hw-04


# Task 1. Extending the Functionality of the Prefix Tree



Implement two additional methods for the Trie class:



count_words_with_suffix(pattern) to count the number of words that end with the given pattern;
has_prefix(prefix) to check whether there are any words with the given prefix.




Technical Requirements



The Homework class should inherit from the base Trie class.
The methods should handle input errors for invalid data.
The input parameters for both methods should be strings.
The count_words_with_suffix method should return an integer.
The has_prefix method should return a boolean value.




Acceptance Criteria



📌 The acceptance criteria for the homework assignment are a mandatory condition for the mentor to review the task.


The count_words_with_suffix method returns the number of words that end with the given pattern. If no words match, it returns 0. It considers case sensitivity (10 points).
The has_prefix method returns True if there is at least one word with the given prefix. It returns False if no such words exist. It considers case sensitivity (10 points).
The code passes all tests (10 points).
Invalid input data is handled properly (10 points).
The methods work efficiently on large datasets (10 points).


Program Template



from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        pass

    def has_prefix(self, prefix) -> bool:
       pass

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Check for words that end with the given suffix
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Check for prefix existence
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat





# Task 2. Finding the Longest Common Prefix



Create a LongestCommonWord class that inherits from the Trie class and implement the find_longest_common_word method, which finds the longest common prefix for all the words in the input array of strings strings.



Technical Requirements



The LongestCommonWord class must inherit from Trie.
The input parameter of the find_longest_common_word method, strings, is an array of strings.
The find_longest_common_word method should return a string – the longest common prefix.
The time complexity is 
O
(
S
)
O(S) , where 
S
S is the total length of all the strings.


Acceptance Criteria



1. The find_longest_common_word method:

Returns the longest common prefix shared by all words (10 points),
Returns an empty string if there is no common prefix (10 points),
Correctly handles an empty array or invalid input data (10 points).
2. The code passes all tests (20 points).



Program Template



from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        pass

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""