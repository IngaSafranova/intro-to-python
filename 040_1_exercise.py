# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

# remove words that are shorter that 10 or with -
# words that more than 15 char to shorten with ... at the end
# format to the string

def report_long_words(words):
  # pass
  long_words = long_words_only(words)
  shortened_words = func_to_shorten(long_words)
  string = formated_shotened_words(shortened_words)
  return string
 
 
 
def long_words_only(words):
  # remove words that are shorter that 10 or with -
   long_words_list = []
   for word in words:
     if len(word) > 10 and '-' not in word:
       long_words_list.append(word)
   return long_words_list
 
print(long_words_only(['hello',
   'nonbiological',
  'Kay',
  'this-is-a-long-word',
  'antidisestablishmentarianism']))
print("Function: long_words_only(words)")
 
def func_to_shorten(words):
 # words that more than 15 char to shorten with ... at the end
 shortened_words_list = []
 for word in words:
   if len(word) > 15:
     shortened_word = word[0:15] +'...'
     shortened_words_list.append(shortened_word)
   else:
     shortened_words_list.append(word)
 return shortened_words_list
   
  
print(func_to_shorten([
   'nonbiological',
  'antidisestablishmentarianism']))
print("Function: func_to_shorten")

def formated_shotened_words(words):
 # format to the string
 result = 'These words are quite long: '
 for word in words:
   if word != words[-1]:
     result += f'{word}, '
   else:
     result += f'{word}'
 return result
 
 
print(formated_shotened_words([
   'nonbiological',
  'antidisestablis...']))
print("Function: formated_shotened_words")


check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
