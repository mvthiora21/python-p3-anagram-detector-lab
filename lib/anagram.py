# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)
        return [anagram for anagram in possible_anagrams if sorted(anagram) == sorted_word]