# Spark-Queries-for-MoviesDB
In particular in this work we will deal with and see in practice (hands-on) data management using open source tools, and in particular the Apache Spark and Apache Kafka frameworks (for Data Streaming).

>## Data
In this work, the dataset consists of four .csv files. The files can be downloaded from Kaggle and relate to the MovieLens Dataset 20M, in particular:
- Tag.csv: contains tags applied by users to movies (about 465000 trags)
- Movies.csv: contains movie information (approximately 27000 movies in period 1995 to 2015).
- Rating.csv: contains user ratings for movies (approximately 20000000)
- genome_tags.csv: contains the IDs and descriptions of the tags 

Data URL: https://www.kaggle.com/grouplens/movielens-20m-dataset

>## Question 1: Execute queries
Run the following queries, using different configurations for Spark. Start with a simple single node machine (local, all cores) and implement the following queries in Python. <br>
Questions to implement: <br />
1. Give the number of users who saw the movie "Jumanji". 
2. Give the names of the movies that users have marked as "boring".
3. Give users who have rated the movie "Bollywood" and have rated with a score > 3.
4. Find the top 10 movies for each year.
5. Give the labels for each movie and the name of the movie for the year 2015.
6. Give the number of ratings for each movie.
7. Find the top 10 users with the most ratings for each year.
8. Find the movies with the most ratings for each movie category.
9. Give all users watching the same movie the same day and time.
10. Give the number of movies, for each category, that users marked as "Funny" and with a rating > 3.5.

>## Question 2: Comparison of performance in single node / virtual cluster / Livy
Set Spark to start with 1 master and two worker threads, thus creating
a virtual cluster on your machine.
1. Execute the above 10 queries, noting the execution time of the queries. The combinations you will be able to choose depend on the capabilities of the machine your. In each case, explore the runtime with THREE combinations of settings.
2. Perform the above queries on the Livy Server available for the course. Note the execution times of the queries.
3. Compare the observed query execution times in the various configurations you used. What do you consider to be the reason for the existence (or non-existence) of observations?

