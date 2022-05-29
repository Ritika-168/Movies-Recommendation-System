# Movies-Recommendation-System
I have created a Movie Recommendation System which recommends and predicts all the hollywood english movies that user wants to search <br/>
## Types of recommendation System
Popularity Based: It keeps a track of view counts for each movie/video and then lists movies based on views in descending order.

Content Based: This type of recommendation system, takes in a movie that a user currently likes as input. Then it analyzes the contents of the movie to find out other movies which have similar content. Then it ranks similar movies according to their similarity scores and recommends the most relevant movies to the user.

Collaborative filtering: In this category, the recommendations get filtered based on the collaboration between similar user’s preferences.
## DataSets
Here i have used two different datasets <br/>
1) TMDB 5000 movies dataset<br/>
2) Movie credits.csv

# Algorithm Used 
i have used Count Vectorisation Cosine Similarity Algorithm which is suggesting movies on the basis of tags and popularity.<br/>
Indirectly  It is recommwnding movies in the basis of searching first and then Sorting..<br/>
Cosine similarity is a metric used to measure how similar two items are. Mathematically it calculates the cosine of the angle between two vectors projected in a multidimensional space. Cosine similarity is advantageous when two similar documents are far apart by Euclidean distance(size of documents) chances are they may be oriented closed together. The smaller the angle, higher the cosine similarity<br/>
1 - cosine-similarity = cosine-distance

Check out the url for demo -- https://movies-recommending.herokuapp.com/
### Technologies Used
Python <br/>
Machine Learning 
#### Frameworks and Library<br/>
Numpy <br/>
Pandas<br/>
Streamlit<br/>
Pickle<br/>
