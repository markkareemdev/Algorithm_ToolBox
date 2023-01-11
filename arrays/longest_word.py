
# Longest Word
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"


# Examples
# Input: "fun&!! time"
# Output: time



def LongestWord(sen):

  # code goes here
  alpha_signs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
  new_word = ''.join([i for i in sen if i in alpha_signs]).split(" ")

  word_freq = [len(word) for word in new_word]
  finder_num=sorted(word_freq,reverse=True)[0]
  locator = word_freq.index(finder_num)

  return new_word[locator]