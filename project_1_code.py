# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:38:45 2024

@author: JEMIMA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#pd.reset_option('all')

"""
Data cleaning Steps
#Load csv file
df = pd.read_csv("movie_dataset.csv")

#pd.reset_option('display.max_columns') 

#Renaming columns Runtime (Minutes) and Revenue (Millions)
df.columns = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime_minutes',
             'Rating', 'Votes', 'Revenue_millions', 'Metascore']

#Dropping Rank column
df.drop(['Rank'], inplace=True, axis=1)

#Changing Year to proper integer format
df['Year'] = df['Year'].astype(int) 

#There are some few empty cells the Revenue_millions column so I'm finding the mean and using that to replace em
revenue_ave = df["Revenue_millions"].mean()
df["Revenue_millions"].fillna(revenue_ave, inplace=True)

#Doing same for metascore column
metascore_ave = df["Metascore"].mean()
df["Metascore"].fillna(metascore_ave, inplace=True)

# Create a new 'Rank' column starting from 1
df['Rank'] = df.index + 1
#making this Rank the first column
df = df[['Rank'] + [col for col in df.columns if col != 'Rank']]

#Saving(loading) the cleaned data removing the panda index
df.to_csv("movie_dataset_cleaned.csv", index=False)
#print(df_clean)

"""


#Now solving to the questions using the cleaned data
df_clean = pd.read_csv("movie_dataset_cleaned.csv")


"""
Question 1
What is the highest rated movie in the dataset?

python output
54    The Dark Knight
Name: Title, dtype: object
"""

#Find the highest rating
#print(df_clean['Rating'].max())
print('Question 1: The Highest rated movie is:')
print(df_clean['Title'][df_clean['Rating'] == 9.0].astype(str))

"""
What is the average revenue of all movies in the dataset? 

python output
82.95637614678898
"""

print('\nQuestion 2: The average revenue of all movies in the dataset is')
print(df_clean['Revenue_millions'].mean().round(3))



"""
Question 3

What is the average revenue of movies from 2015 to 2017 in the dataset?
Note, since the answer will be effected by how you dealt with missing values a range has been provided. 

python output
63.44658789732184
"""

# Figuring out unique values in the 'Year' column
#print("Unique values in 'Year':", df_clean['Year'].unique())
#Unique values in 'Year': [2014 2012 2016 2015 2007 2011 2008 2006 2009 2010 2013]

# Filter the DataFrame for years greater than 2015 only
filtered_ave_revenue = df_clean['Revenue_millions'][df_clean['Year'] > 2015]

# Find the avereage filtered DataFrame
print('\nQuestion 3: The average revenue of movies from 2015 to 2017 is')
print(filtered_ave_revenue.mean().round(3))



"""
Question 4

How many movies were released in the year 2016?

python output
297
"""

#Filtering the number of movies released in year 2016
movies_2016 = df_clean[df_clean['Year'] == 2016]

print('\nQuestion 4: The number of movies released in the year 2016')
print(len(movies_2016))


"""
Question 5

How many movies were directed by Christopher Nolan?

python output
5
"""

#Filtering out the number of movies released by Christopher Nolan
chris_movies = df_clean[df_clean['Director'] == 'Christopher Nolan']

print('\nQuestion 5: The number of movies released by Christopher Nolan are')
print(len(chris_movies))


"""
Question 6

How many movies in the dataset have a rating of at least 8.0?

python output
78
"""

#Filtering out the number of movies with a rating of 8.0 and more
rating_least_8 = df_clean[df_clean['Rating'] >= 8.0]
print('\nQuestion 6: The number of movies with a rating of 8.0 and more are:')
print(len(rating_least_8))


"""
Question 7

What is the median rating of movies directed by Christopher Nolan?

python output
8.680000000000001
"""
 
#Filtering the median rating of movies Directed by Christopher Nolan
chris_movies_rating = df_clean['Rating'][df_clean['Director'] == 'Christopher Nolan']
print('\nQuestion 7: The median rating of movies directed by Christopher Nolan are:')
print(chris_movies_rating.mean().round(3))


"""
Question 8

Find the year with the highest average rating?

python output
2007
"""

average_ratings = df_clean.groupby('Year')['Rating'].mean()
average_ratings_1dec = average_ratings.round(6)
#print(average_ratings_1dec)
"""
2006    7.1
2007    7.1
2008    6.8
2009    7.0
2010    6.8
2011    6.8
2012    6.9
2013    6.8
2014    6.8
2015    6.6
2016    6.4
Name: Rating, dtype: float64
"""

#idxmax() returns the index (year) of the maximum average rating.
highest_avg_rating_year = average_ratings_1dec.idxmax() 
max_ave_rating = average_ratings_1dec.max()
print('\nQuestion 8: The year with the highest rating')
print(highest_avg_rating_year)


"""
Question 9

What is the percentage increase in number of movies made between 2006 and 2016?

python output
575.0
"""
#Find movies made in 2006 and 2016
count_2006 = len(df_clean[df_clean['Year'] == 2006])
count_2016 = len(df_clean[df_clean['Year'] == 2016])
#print(count_2006)
#44
#print(count_2016)
#297

#percentage increase
percentage_increase = (count_2016-count_2006)/count_2006 * 100

print('\nQuestion 9: Thepercentage increase of movies made between 2006 and 2016')
print(percentage_increase)


"""
Question 10
Find the most common actor in all the movies?

Note, the "Actors" column has multiple actors names. You must find a way to search for the most common actor in all the movies.

python output
Mark Wahlberg
"""
#Making the actors column an array on individual names that can be iterated through
df_clean['Actors'] = df_clean['Actors'].apply(lambda x: x.split(', '))

np_actors = np.array(df_clean['Actors'])

flattened_actors = [actor for sublist in np_actors for actor in sublist]

#Making the arrays into numpy arrays for easy analysis

np_flattened_actors = np.array(flattened_actors)

unique_actors, counts = np.unique(np_flattened_actors, return_counts=True)

most_frequent_index = np.argmax(counts)
most_frequent_actor = unique_actors[most_frequent_index]
most_frequent_count = counts[most_frequent_index]

print('\nQuestion 10: The most common actor in all the movies is')
print(most_frequent_actor)


"""
Question 11
How many unique genres are there in the dataset?

Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.

python output
20
"""
#Making the genre column an array on individual names that can be iterated through
df_clean['Genre'] = df_clean['Genre'].apply(lambda x: x.split(','))

np_genre = np.array(df_clean['Genre'])

flattened_genre = [genre for sublist in np_genre for genre in sublist]

#Making the arrays into numpy arrays for easy analysis

np_flattened_genre = np.array(flattened_genre)

unique_genre = np.unique(np_flattened_genre)

print('\nQuestion 11: The number of unique genres are')
print(len(unique_genre))
print(unique_genre)


"""
# Step 1: Flatten the array of actors
flattened_actors = np.concatenate(np_actors)
# Step 2: Count occurrences of each actor
unique_actors, counts = np.unique(flattened_actors, return_counts=True)

# Step 3: Find the most famous actor (the one with the highest count)
most_famous_actor_index = np.argmax(counts)
most_famous_actor = unique_actors[most_famous_actor_index]
most_famous_actor_count = counts[most_famous_actor_index]

print(f"The most famous actor is: {most_famous_actor} with {most_famous_actor_count} appearances.")
"""

"""
Question 12
Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights.

And what advice can you give directors to produce better movies?
"""

#print(df_clean.describe())

#Selecting only the numerical columns of this data set for numerical analysic
numeric_df = df_clean.select_dtypes(include=['number'])
 
# Calculate the correlation matrix for the cleaned numeric columns
correlation_matrix = numeric_df.corr()
filtered_correlation = correlation_matrix[(correlation_matrix > 0.4) | (correlation_matrix < -0.4)]

print('\nThe correlation matrix is')
print(correlation_matrix)

print('\nThe plot for the correlation ')

plt.figure(figsize=(10, 8))
sns.heatmap(filtered_correlation, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
#plt.show()


#Finding the average run time of movies with a rating of 9 and above
print('\nThe average run time opf movies with rating 9 and above is')
print(df_clean['Runtime_minutes'][df_clean['Rating'] >= 9].mean())

#Finding the average run time of movies with a rating of 8 and above
print('\nThe average run time opf movies with rating 8 and above is')
print(df_clean['Runtime_minutes'][df_clean['Rating'] >= 8].mean())

# Step 1: Filter movies with a rating of 7 and above
df_high_rating = df_clean[df_clean['Rating'] >= 7]

np_genre = np.concatenate(df_high_rating['Genre'].dropna().values)

unique_genre, countsgen = np.unique(np_genre, return_counts=True)

# Step 4: Create a DataFrame to hold genres and their counts
genre_counts = pd.DataFrame({'Genre': unique_genre, 'Count': countsgen})

# Step 5: Sort the DataFrame by counts in descending order
top_genres = genre_counts.sort_values(by='Count', ascending=False)

# Step 6: Get the top 5 popular genres
top_5_genres = top_genres.head(5)

# Step 7: Print the top 5 genres
print('\nThe top 5 genres are')
print(top_5_genres)

"""
 Genre  Count
6       Drama    286
1   Adventure    116
0      Action    114
4      Comedy    105
17   Thriller     81
"""




"""
                      Rank      Year  Runtime_minutes    Rating     Votes  \
Rank              1.000000 -0.261605        -0.221739 -0.219555 -0.283876   
Year             -0.261605  1.000000        -0.164900 -0.211219 -0.411904   
Runtime_minutes  -0.221739 -0.164900         1.000000  0.392214  0.407062   
Rating           -0.219555 -0.211219         0.392214  1.000000  0.511537   
Votes            -0.283876 -0.411904         0.407062  0.511537  1.000000   
Revenue_millions -0.252996 -0.117562         0.247834  0.189527  0.607941   
Metascore        -0.185159 -0.076077         0.202239  0.604723  0.318116   

                  Revenue_millions  Metascore  
Rank                     -0.252996  -0.185159  
Year                     -0.117562  -0.076077  
Runtime_minutes           0.247834   0.202239  
Rating                    0.189527   0.604723  
Votes                     0.607941   0.318116  
Revenue_millions          1.000000   0.132304  
Metascore                 0.132304   1.000000  
"""


"""
For raw unfiltered data
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   c             1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None

For column names changes and rank removed

RangeIndex: 1000 entries, 0 to 999
Data columns (total 11 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Title             1000 non-null   object 
 1   Genre             1000 non-null   object 
 2   Description       1000 non-null   object 
 3   Director          1000 non-null   object 
 4   Actors            1000 non-null   object 
 5   Year              1000 non-null   int64  
 6   Runtime_minutes   1000 non-null   int64  
 7   Rating            1000 non-null   float64
 8   Votes             1000 non-null   int64  
 9   Revenue_millions  872 non-null    float64
 10  Metascore         936 non-null    float64
dtypes: float64(3), int64(3), object(5)
memory usage: 86.1+ KB
None


Cleaned data .info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Rank              1000 non-null   int64  
 1   Title             1000 non-null   object 
 2   Genre             1000 non-null   object 
 3   Description       1000 non-null   object 
 4   Director          1000 non-null   object 
 5   Actors            1000 non-null   object 
 6   Year              1000 non-null   int64  
 7   Runtime_minutes   1000 non-null   int64  
 8   Rating            1000 non-null   float64
 9   Votes             1000 non-null   int64  
 10  Revenue_millions  1000 non-null   float64
 11  Metascore         1000 non-null   float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
None

df_clean.info()
              Rank         Year  Runtime_minutes       Rating         Votes  \
count  1000.000000  1000.000000      1000.000000  1000.000000  1.000000e+03   
mean    500.500000  2012.783000       113.172000     6.723200  1.698083e+05   
std     288.819436     3.205962        18.810908     0.945429  1.887626e+05   
min       1.000000  2006.000000        66.000000     1.900000  6.100000e+01   
25%     250.750000  2010.000000       100.000000     6.200000  3.630900e+04   
50%     500.500000  2014.000000       111.000000     6.800000  1.107990e+05   
75%     750.250000  2016.000000       123.000000     7.400000  2.399098e+05   
max    1000.000000  2016.000000       191.000000     9.000000  1.791916e+06   

       Revenue_millions    Metascore  
count       1000.000000  1000.000000  
mean          82.956376    58.985043  
std           96.412043    16.634858  
min            0.000000    11.000000  
25%           17.442500    47.750000  
50%           60.375000    58.985043  
75%           99.177500    71.000000  
max          936.630000   100.000000 
"""
