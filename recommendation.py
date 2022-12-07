from scipy import spatial
import pandas as pd
import operator
import numpy as np
import json

# The Hunger Games
# find similarity between two books
def Similarity(bookId1, bookId2):
    try:
        a = books.iloc[bookId1]
        b = books.iloc[bookId2]

        genresA = json.loads(a['genres_bin'])
        genresB = json.loads(b['genres_bin'])

        genreDistance = spatial.distance.cosine(genresA, genresB)

        authorA = json.loads(a['authors_bin'])
        authorB = json.loads(b['authors_bin'])

        authorDistance = spatial.distance.cosine(authorA, authorB)

        if genreDistance + authorDistance:
            return genreDistance + 0.3 * authorDistance
        else:
            return 3.0
    except:
        return 3.0

# find books for recommendation
class SearchNeighbours:
    def __init__(self):
        self.i = 0

    # input a book and find it's index in table
    def enter_book(self):
        name = input('Enter a book title: ')
        new_book = books[books['book_title'].str.contains(name)].iloc[0].to_frame().T
        return new_book.index[0]

    def get_neighbors(self, basebook_index, K):
        distances = []
        for index, book in books.iterrows():
            self.i = self.i + 1
            print(self.i)
            # print('basebook_index', basebook_index)
            # print('index', index)
            dist = Similarity(basebook_index, index)
            distances.append((index, dist))
        distances = list(filter(lambda x: x is not None, distances))
        distances.sort(key=operator.itemgetter(1))
        print(distances)
        neighbors = []

        for x in range(K):
            neighbors.append(distances[x])
        return neighbors


# read dataset
books = pd.read_csv('processed_table.csv')

sn = SearchNeighbours()

K = 10
avgRating = 0
new_book_index = sn.enter_book()
neighbors = sn.get_neighbors(new_book_index, K)
print(neighbors)
print('\nRecommended books: \n')

# for every neighbor print info about similarity with input book, genre and rating
for neighbor in neighbors:
    avgRating = avgRating + float(books.iloc[neighbor[0]][3])
    print(books.iloc[neighbor[0]][6] + " | Similarity: " + str(neighbor[1]) + " | Genres: " + str(
        books.iloc[neighbor[0]][7]).strip('[]').replace(' ', '') + " | Rating: " + str(books.iloc[neighbor[0]][3]))
    print('\n')

print('\n')
# predict rating of input book
avgRating = avgRating / K
print('The predicted rating for %s is: %f' % (books['book_title'].values[new_book_index], avgRating))
print('The actual rating for %s is %f' % (books['book_title'].values[new_book_index], books['book_rating'].values[0]))