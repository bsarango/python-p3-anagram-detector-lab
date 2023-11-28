# your code goes here!


class Anagram:
    def __init__(self,word):    #taking in self and word as the parameter when a instance is made
        self.word = word
    
    def match(self,anagrams):
        
        confirmed_anagrams=[] #list of anagrams if there are any
        split_word = list(self.word)
        split_word.sort()
        for anagram in anagrams:
            split_anagram = list(anagram)
            split_anagram.sort()
            if split_word == split_anagram:
                confirmed_anagrams.append(anagram)
        return confirmed_anagrams