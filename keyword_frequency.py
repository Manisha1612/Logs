
# coding: utf-8

# In[1]:


#python program to find the frequency of keywords from text file/log files
import re
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

frequency = {}
document_text = open('sample.log', 'r')
text_string = document_text.read().lower()
match_pattern1 = re.findall(r'\b[a-z]{3,15}\b', text_string)

stopWords = set(stopwords.words('english'))

#match_pattern =word_tokenize(match_pattern1)
#print(match_pattern1) 
match_pattern = []
for w in match_pattern1:
    if w not in stopWords:
       match_pattern.append(w)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
   # if frequency[words]>50:
        print (words, frequency[words])

