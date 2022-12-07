Data Science Master class: Advanced software engineering
University: Berliner Hochschule für Technik (BHT)
Project name: Book recommendation system
Project author: Polina Kozyr


1. PROJECT DESCRIPTION
The goal of the project is to create a book recommendation system based on the concept of content base filtering.
The user enters a book or several books that he has read, and recommendations are displayed based on the genre, authors and keywords (I'll try my best) of the book.

2. FILES DESCRIPTION
The book folder contains the dataset and marked up photos of the books
File dataset_preprocessing preprocesses the csv file with books so that the data is convenient for analysis when searching for a recommended book
The keywords_processing file contains an algorithm for processing book descriptions, but at the moment the code is under development
The recommendation file contains the recommendation algorithm.

3. DATASET DESCRIPTION
Dataset with 54000 plus books
Metadata can be found here:
https://www.kaggle.com/datasets/meetnaren/goodreads-best-books?select=book_data.csv

4. WHAT HAS BEEN DONE SO FAR
The system has been implemented, however, the recommendation so far is made only on the basis of genre and authors. I wasted a lot of time trying to process book descriptions to also include this data in the recommendation process. But unfortunately it takes a very long time. Using Threading, I managed to significantly reduce the processing time for a dataset with books, according to my calculations, the preprocessing of book descriptions should take about 36 minutes (it won’t take that long to wait for a recommendation, this is just a dataset preprocessing, then I’ll just save it and when issuing a recommendation I will use ready). However, no matter how much I waited, the code execution did not complete. Most likely, the way I process book descriptions is too computationally expensive. I have ideas on how to do the processing of descriptions, however, this still needs time.
I decided to start with the development of the system and see if my algorithm works at all, as I was afraid that I would not be able to make the idea of book recommendations at all. But it seems to work, since now I can work on improvement, DDD, clean code, metrics, etc. Unfortunately, I did not have time to start these sections early, because I wanted to first of all check whether the algorithm works according to the recommendations. And I was very stuck at the moment with the processing of descriptions for books and the creation of a word cloud.

5. KEY ISSUES TO BE INPROVED
 * Still do the processing of book descriptions and also use this data to issue a recommendation 
 * Make issuing recommendations to the user faster. 
 * Make sure that the list of recommended books contains no more than three books by the author of the original book 
 * Improve the code, make it cleaner

6. UML DIAGRAMS
I made the following UML diagrams:
* Use_case_diagram
https://github.com/polinatrump/Book_recommendation_system/blob/main/Use_case_diagram.svg
* Activity_diagram

* Object_diagram

