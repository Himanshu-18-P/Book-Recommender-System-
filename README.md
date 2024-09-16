# Book Recommender System
Book Recommender System | Collaborative Filtering

## file info 
## model file 
   ### data : contains the data of books , rating , user 
   ### recommender.ipynb : this file is for eda , data cleaning , model prepration
   
## Recommendation critaria
   ### Popularity based 
   ### idea : top 50 books with total rating > 250 and with highest rating
   
   ### Collaborative Filtering 
   ### idea : create a data frame column as user and books name as row   
        - books with minimun rating 50 
        - user with number of minimum rating 200
        - then cosin similarity for most similar books

   ### .pkl file is our model after eda and tarning 

## install the requirements 
   ### using [pip install -r requirements.txt]

## to run the file using [python app.py]

