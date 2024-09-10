# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

def LongestWord(sen):

  max_lenght = 0
  # make string to list
  sen_list = sen.split(' ')
  #print(sen_list)
  
  # go throug list word by word
  for word in sen_list:
    
       words = ''
       # check each word for puct char
       for char in word:
        if char.isalnum():
         words = ''.join([words, char])
         # check the lenght
       word_lenght = len(words)
       print(word_lenght)
       print('this is words',words)
       
       # if word lenght is longer than the one in list swap
   
      
       if word_lenght > max_lenght:
         max_lenght = word_lenght
         longest_word = word
  #print('this is l', max_lenght)
  return longest_word
    
         

  

# keep this function call here 
print(LongestWord( "I love dogs"))