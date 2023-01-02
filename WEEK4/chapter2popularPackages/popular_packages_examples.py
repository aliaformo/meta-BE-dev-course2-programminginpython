import json

# NUMPY
import numpy as np

#The zeros() function inside numpy creates an array with n number of zeroes inside it.
a = np.zeros(10)
print(a) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# The full() function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.
b = np.full((2,10), 0.7)
print(b)
# [[0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]
#  [0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7 0.7]]

# In the example, linspace() function divides the values between 0 and 25 in 7 equal parts. 
c = np.linspace(0,25,7)
print(c)
# [ 0.          4.16666667  8.33333333 12.5        16.66666667 20.83333333
# 25.        ]

# data type of c, it is a special data-type created and used in numpy called as ndarray
print(type(c))  # <class 'numpy.ndarray'>


# PANDAS
import pandas as pd

# The first output is for the DataFrame called a that displays the output in a very systematic format.
a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})

print(a)

# The second output uses the describe() function in pandas that will give the count, frequency, top values and frequency among other values.
print(a.describe())

# In the second DataFrame, b consists of letters and numbers in random order.
b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })

# The third output is a sorting function that will provide a sorted table leading to shuffling of the data entries in the table.
print(b.sort_values(by="Numbers"))

# Lastly, the assign() function takes the values present inside the table, performs an operation over them and creates a new variable called new_values that is then added to the table.
b = b.assign(new_values = b['Numbers']*3)
print(b)

"""
    Animals   Sounds
0       Dog    Barks
1       Cat     Meow
2      Lion    Roars
3       Cow      Moo
4  Elephant  Trumpet
       Animals Sounds
count        5      5
unique       5      5
top        Dog  Barks
freq         1      1
  Letters  Numbers
5       f        1
3       d        3
4       e        5
1       b        7
2       c        9
0       a       12
  Letters  Numbers  new_values
0       a       12          36
1       b        7          21
2       c        9          27
3       d        3           9
4       e        5          15
5       f        1           3

"""


# NLTK  is a library in Python used for Natural Language Processing
import nltk

# First a block of text is copied inside the code-block and assigned to a variable called text.
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Print statement 1
# The first function used is word_tokenize(). This takes this text and produces the first part of the output in which the words are ‘tokenized’ or simply separated by a whitespace
print(word_tokenize(text))

# Print statement 2
# The second function sent_tokenize() takes this block of text and tokenizes by ‘sentences’.
print(nltk.tokenize.sent_tokenize(text))


stopwords = stopwords.words("english")
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

"""For the third output, I first split the code and remove what is called ‘stopwords’. Stopwords are words in the English language that can be considered redundant and adding little value while you are undertaking natural language processing. These include words such as ‘a’, ‘the’, ‘him’. First I'll create a list of these stopwords and then remove them using a for loop to form a new list called new_text. """

# Print statement 3
print(new_text)

# ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.']

# ['Lorem Ipsum is simply dummy text of the printing and typesetting industry.', "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."]

# ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry.', 'Lorem', 'Ipsum', "industry's", 'standard', 'dummy', 'text', 'ever', 'since', '1500s,', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book.']
