from typing import List, Set

import pandas as pd
from utils import parse


class ContentBaseRecSys:

    def __init__(self, movies_dataset_filepath: str, distance_filepath: str):
        self.distance = pd.read_csv(distance_filepath, index_col='movie_id')
        self.distance.index = self.distance.index.astype(int)
        self.distance.columns = self.distance.columns.astype(int)
        self._init_movies(movies_dataset_filepath)

    def _init_movies(self, movies_dataset_filepath) -> None:
        self.movies = pd.read_csv(movies_dataset_filepath, index_col='id')
        self.movies.index = self.movies.index.astype(int)
        self.movies['genres'] = self.movies['genres'].apply(parse)

    def get_title(self) -> List[str]:
        return self.movies['original_title'].values

    def get_genres(self) -> Set[str]:
        genres = [item for sublist in self.movies['genres'].values.tolist() for item in sublist]
        return set(genres)
    
    def get_year(self) -> List[str]:
        return self.movies['release_date'].values

    def recommendation(self, title: str, top_k: int = 5, genre_filter: str = None, param_filter: str = None) -> List[str]:
        """
        Returns the names of the top_k most similar movies with the movie "title" after applying filters
        """
        filtered_movies = self.movies.copy()
        
              
        filtered_movies = filtered_movies[filtered_movies['genres'].apply(lambda x: genre_filter in x)]
        
        filtered_movies = filtered_movies[filtered_movies['release_date'] == param_filter]
        
        if filtered_movies.empty:
            return []

        movie_ids = filtered_movies[filtered_movies['original_title'] == title].index
        
        if len(movie_ids) == 0:
            return []

        movie_id = movie_ids[0]
        similar_movies = self.distance.loc[movie_id].sort_values()[1:top_k+1]
        similar_movie_ids = similar_movies.index.tolist()
        similar_movie_names = self.movies.loc[similar_movie_ids]['original_title'].tolist()

        return similar_movie_names
