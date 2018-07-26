"""
Please write a script that takes a list of words
and returns the longest word.  For example:
[‘city’,’state’,’zip’,’address’,’name’].  The script needs
to figure out which is the longest word and
print out the word, as well as the word length.
"""

words = ['city', 'state', 'zip', 'address', 'name', 'prettyLongWord']

length = 0
longest_word_length = 0
for word in words:
    length = len(word)
    if length > longest_word_length:
        longest_word_length = length
        longest_word = word

print('List of words', words)
print('Longest word in list: ', longest_word, '\nLength of longest word: ',longest_word_length)
