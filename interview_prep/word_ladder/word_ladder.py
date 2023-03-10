import subprocess
import sys
from collections import deque

#grab English words
subprocess.check_call([sys.executable, "-m", "pip", "install", 'english-words'])
from english_words import english_words_set 

class WordLadder:
    
    def __init__(self, first_word, second_word):
        if not first_word.isalpha():
            raise Exception("Only English A to Z in first_word")
        if not second_word.isalpha():
            raise Exception("Only English A to Z in second_word")
        if len(first_word) != len(second_word):
            raise Exception("both words must be the same length")
        

        
        self.first_word = first_word
        self.second_word = second_word
        self.words = english_words_set
        self.letters = ['a','b','c','d','e','f','g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

    def remove_at(self,i, s):
        return s[:i] + s[i+1:]

    def add_at(self,i,a, s):
        return s[:i] + a + s[i:]

    def is_second_word(self,string):
        if string == self.second_word:
            return True
        return False

    def is_first_word(self,string):
        if string == self.first_word:
            return True
        return False

    def run(self):

        steps = []
        # Find length of string
        sting_length = len(self.first_word)

        for a in range(sting_length):
            loop_list = []
            #letter = self.first_word[a]
            base = self.remove_at(a, self.first_word)

            for b in self.letters:
                new_word = self.add_at(a, b, base)
                #validate
                if new_word in english_words_set:
                    loop_list.append(new_word)
            
            unique_list = list(set(loop_list))
            try:
                unique_list.remove(self.first_word)
            except ValueError:
                pass

            if len(unique_list) == 0:
                raise Exception("We can not compute a new word")
            steps.append(unique_list)

            if self.second_word in unique_list:
                word_found = True
                break

        return {
            "max_steps": len(steps),
            "steps": steps
            }

# tree = WordLadder("trees", "tests")
# print(tree.run())



# Python3 program to find length of the
# shortest chain transformation from source
# to target
from collections import deque
 
# Returns length of shortest chain
# to reach 'target' from 'start'
# using minimum number of adjacent
# moves. D is dictionary
def word_ladder(start_word, target_word, word_dict):

    if not start_word.isalpha():
        raise Exception("Only English A to Z in start_word")
    if not target_word.isalpha():
        raise Exception("Only English A to Z in target_word")
    if len(start_word) != len(target_word):
        raise Exception("both words must be the same length")
    if target_word not in word_dict:
        raise Exception("Target word is not an English word")
    if start_word not in word_dict:
        raise Exception("Starting word is not an English word")
    
    #Corner case
    if start_word == target_word:
      return 0

     # To store the current chain length
    # and the length of the words
    level = 0
    wordlength = len(start_word)
    letters = ['a','b','c','d','e','f','g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
 
    # Push the starting word into the queue
    Q =  deque()
    Q.append(start_word)
 
    # While the queue is non-empty
    while (len(Q) > 0):
         
        # Increment the chain length
        level += 1
 
        # Current size of the queue
        sizeofQ = len(Q)
        for i in range(sizeofQ):
 
            # Remove the first word from the queue
            word = [j for j in Q.popleft()]
            #Q.pop()
 
            # For every character of the word
            for pos in range(wordlength):
                 
                # Retain the original character
                # at the current position
                orig_char = word[pos]
 
                # Replace the current character with
                # every possible lowercase alphabet
                for c in range(len(letters)):
                    word[pos] = letters[c]
 
                    # If the new word is equal
                    # to the target word
                    if ("".join(word) == target_word):
                        return level + 1
 
                    # Remove the word from the set
                    # if it is found in it
                    if ("".join(word) not in word_dict):
                        continue
                         
                    del word_dict["".join(word)]
 
                    # And push the newly generated word
                    # which will be a part of the chain
                    Q.append("".join(word))
 
                # Restore the original character
                # at the current position
                word[pos] = orig_char
 
    return 0
 
# Driver code
if __name__ == '__main__':

    start = "high"
    target = "help"
    print("Length of shortest chain is: ",
    word_ladder(start, target, dict.fromkeys(english_words_set,1)))
 
