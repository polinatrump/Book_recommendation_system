from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
import pandas as pd
from threading import Thread

# nltk.download('stopwords')
# nltk.download('punkt')



def binary_words(descript):
    try:
        descript = [i.lower() for i in descript]
        binary_list = [0] * len(unique_words)
        threads = [None] * len(descript)
        for word_index in range(len(descript)):
            threads[word_index] = Thread(target=search_word, args=(descript[word_index], binary_list))
            threads[word_index].start()
        for i in threads:
            i.join()
        return binary_list
    except:
        pass


def search_word(word, binary_list):
    #     print(word)
    if word:
        if word[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            word_value = vocabulary[word[0]].get(word)
            if word_value:
                binary_list[word_value] = 1
        else:
            word_value = vocabulary['other'].get(word)
            if word_value:
                binary_list[word_value] = 1





# read dataset
full_books_table = pd.read_csv('books/book_data.csv')

# delete useless columns
books = full_books_table.drop(['book_edition', 'book_format', 'book_isbn', 'book_pages'], axis=1)

# create word cloud
plt.subplots(figsize=(12,12))

# load words that we don't want algorithm work with
stop_words = set(stopwords.words('english'))
stop_words.update(',',';','!','?','.','(',')','$','#','+',':','...',' ','','will','shall', 'was', 'were', 'the', 'of', 'about', '-', '.')

words=books['book_desc'].dropna().apply(nltk.word_tokenize)
word=[]
for i in words:
    word.extend(i)
word=pd.Series(word)
word=([i for i in word.str.lower() if i not in stop_words])
wc = WordCloud(background_color="black", max_words=2000, stopwords=STOPWORDS, max_font_size= 60,width=1000,height=1000)
wc.generate(" ".join(word))
plt.imshow(wc)
plt.axis('off')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.show()

# delete some useless signs
word = [i.replace("'",'').replace('"','').replace('#', '').replace('+', '').replace('-', '').replace('.', '').replace(',', '').replace('*', '').replace('&', '').replace('%', '').replace('/', '') for i in word]
word = [i for i in word if len(i) > 0]
unique_words = set(word)
unique_words = sorted(unique_words)

# make a dict where keys are words and values are numbers
words_indx_dict = {}
for i in range(len(unique_words)):
    words_indx_dict[unique_words[i]] = i

# to make code working quicker devide vocabulary for dictionaries where key is first letter
# of the word and values are all the words with this first letter
# also add a group for other words like signs and other things
vocabulary = {}
for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    letter_words = {}
    for key, value in words_indx_dict.items():
        if key[0] == letter:
            letter_words[key] = value
    vocabulary[letter] = letter_words

other_words = {}
for key, value in words_indx_dict.items():
    if key[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        other_words[key] = value
vocabulary['other'] = other_words

# make each description of the book a list of words
books['book_desc'] = books['book_desc'].str.strip('[]').str.replace("'",'').str.replace('"','').str.replace(',','')
books['book_desc'] = books['book_desc'].str.split(' ')

books['desc_bin'] = books['book_desc'].apply(lambda x: binary_words(x))

print(books['desc_bin'])