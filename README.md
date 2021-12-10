# Spark-Queries-for-MoviesDB
In particular in this work we will deal with and see in practice (hands-on) data management using open source tools, and in particular the Apache Spark and Apache Kafka frameworks (for Data Streaming).
## Data
In this work, the dataset consists of four .csv files. The files can be downloaded from Kaggle and relate to the MovieLens Dataset 20M, in particular:
- Tag.csv: contains tags applied by users to movies (about 465000 trags)
- Movies.csv: contains movie information (approximately 27000 movies in period 1995 to 2015).
- Rating.csv: contains user ratings for movies (approximately 20000000)
- genome_tags.csv: contains the IDs and descriptions of the tags 
<br >
Data URL: https://www.kaggle.com/grouplens/movielens-20m-dataset
## Question 1: Execute queries
Run the following queries, using different configurations for Spark. Start with a simple single node machine (local, all cores) and implement the following queries in Python. <br>
Questions to implement:<br>
1. Give the number of users who saw the movie "Jumanji". 

