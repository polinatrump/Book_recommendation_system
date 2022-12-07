import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from threading import Thread


class Binary:
    def __init__(self):
        self.i = 0

    # creating one hot encoded array for genres
    def binary_genres(self, book_genre_list, List):
        binary_list = []
        if type(book_genre_list) == list:
            for genre in List:
                if genre in book_genre_list:
                    binary_list.append(1)
                else:
                    binary_list.append(0)
            return binary_list
        else:
            return None

    # creating one hot encoded array for authors
    def binary_authors(self, authors):
        try:
            self.i = self.i + 1
            print(self.i)
            binary_list = [0] * len(authors_indx_dict)
            threads = [None] * len(authors)
            #         print(threads)
            for author_index in range(len(authors)):
                threads[author_index] = Thread(target=self.search_author, args=(authors[author_index], binary_list))
                threads[author_index].start()
            for i in threads:
                i.join()
            return binary_list
        except:
            pass

    def search_author(self, author, binary_list):
        #         print(author)
        if author:
            author_value = authors_indx_dict.get(author)
            if author_value:
                binary_list[author_value] = 1


# read dataset
full_books_table = pd.read_csv('books/book_data.csv')

# delete useless columns
books = full_books_table.drop(['book_edition', 'book_format', 'book_isbn', 'book_pages'], axis=1)

# make lists of genres for each book
books['genres'] = books['genres'].str.split('|')

# make graph of top genres
plt.subplots(figsize=(12,10))
list1 = []
for i in books['genres']:
    if type(i) ==  list:
        if int(len(i)) != 0:
            list1.extend(i)
ax = pd.Series(list1).value_counts()[:10].sort_values(ascending=True).plot.barh(width=0.9,color=sns.color_palette('hls',10))
for i, v in enumerate(pd.Series(list1).value_counts()[:10].sort_values(ascending=True).values):
    ax.text(.8, i, v,fontsize=12,color='white',weight='bold')
plt.title('Top Genres')
plt.show()

# make Series where indexes are names of genres and values are their unique indexes
genreList = pd.Series(list1).value_counts()

# create a new column in which each value will be a one hot encoded array
# with 1 on the places of indexes of genres that are in each book
binary = Binary()
books['genres_bin'] = books['genres'].apply(lambda x: binary.binary_genres(x, genreList.index))

# print(books['genres_bin'].head())

# make lists of authors for each book
books['book_authors'] = books['book_authors'].str.split('|')

# make graph of top authors
plt.subplots(figsize=(12,10))
list2 = []
for i in books['book_authors']:
    list2.extend(i)
ax = pd.Series(list2).value_counts()[:15].sort_values(ascending=True).plot.barh(width=0.9,color=sns.color_palette('muted',40))
for i, v in enumerate(pd.Series(list2).value_counts()[:15].sort_values(ascending=True).values):
    print(v)
    ax.text(.8, i, v,fontsize=10,color='white',weight='bold')
plt.title('Authors with highest appearance')
plt.show()

# make Series where indexes are names of authors and values are their unique indexes
authorsList = pd.Series(list2).value_counts()

# create a dictionary, where keys are authors and values are thier indexes
authors_indx_dict = {}
for i in range(len(authorsList.index)):
    authors_indx_dict[authorsList.index[i]] = i

# create a new column in which each value will be a one hot encoded array
# with 1 on the places of indexes of authors that wrote each book
books['authors_bin'] = books['book_authors'].apply(lambda x: binary.binary_authors(x))

books.to_csv('processed_table.csv')

# delete signs from words in descriptions for books
word = [i.replace("'",'').replace('"','').replace('#', '').replace('+', '').replace('-', '').replace('.', '').replace(',', '').replace('*', '').replace('&', '').replace('%', '').replace('/', '') for i in word]
word = [i for i in word if len(i) > 0]

# unique_words is a list with ench word that was in descriptions
unique_words = set(word)
unique_words = sorted(unique_words)

# make dict where word is index and index of word is value
words_indx_dict = {}
for i in range(len(unique_words)):
    words_indx_dict[unique_words[i]] = i