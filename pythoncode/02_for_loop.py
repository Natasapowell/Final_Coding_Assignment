
#to enter python, I type python in the shell

#Automating repeating tasks using Python “for” loops.

[i**2 for i in  range(0,10)]

#another example:

textexample = "This is an example text to show that I can use python to automate repeating tasks."

#this next line of code is copied (for simplification), as that was given in another course
punct = [",", ".", ";","'", "?", "&", "!", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

no_punct_text = "" 

for letter in textexample:
    if letter not in punct:
        no_punct_text = string_no_punc + char
print(string_no_punc)

#another example could be for looking at text and seeing the word frequencies
#this is a code I wrote for another class:


def process_string(input_string):
  clean_string = re.sub('[^a-zA-Z\s]+', '', input_string.lower())
  word_list = clean_string.split()
  return word_list

import re

with open('output/wiki_opera_paris.txt', 'r', encoding='utf-8') as file:
    opera_text = file.read() #opening file

word_list = process_string(opera_text) # using function from first exercise

word_freq = {}
for word in word_list:
    word_freq[word] = word_freq.get(word, 0) + 1 # Counting the frequency, using dict 

with open('wiki_opera_counted.txt', 'w', encoding='utf-8') as file:
    for word, freq in word_freq.items():
        file.write(f"{word}, {freq}\n") # creating file with words and frequencies


