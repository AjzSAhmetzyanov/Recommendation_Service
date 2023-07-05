from base import ContentBaseRecSys
 
if __name__ == "__main__":
    rec_sys = ContentBaseRecSys('../assets/movies.csv', '../assets/distance.csv')
    recommendations = rec_sys.recommendation('The Dark Knight', top_k=5)
    print(recommendations)
