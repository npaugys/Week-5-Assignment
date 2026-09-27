'''
BASE LEVEL
Your Movie Collection
---------------------------------------------------
Inception                 2010   Sci-fi / Thriller       8.6
The Shawshank Redemption  1994   Drama                   9.7
The Godfather             1972   Crime / Drama           9.2
The Dark Knight           2008   Action / Crime / Drama  9.0
Pulp Fiction              1994   Crime / Drama           6.5

You will now enter two new movies.

Enter movie title: the wild robot
Enter movie year: 2024
Enter genres (separated by commas): Action, Comedy
Enter movie rating: 6.8

Enter movie title: The shining
Enter movie year: 1980
Enter genres (separated by commas): thrillER, HORRor
Enter movie rating: 9.8

All Movies Sorted by Year
---------------------------------------------------
The Godfather             1972   Crime / Drama           9.2
The Shining               1980   Thriller / Horror       9.8
The Shawshank Redemption  1994   Drama                   9.7
Pulp Fiction              1994   Crime / Drama           6.5
The Dark Knight           2008   Action / Crime / Drama  9.0
Inception                 2010   Sci-fi / Thriller       8.6
The Wild Robot            2024   Action / Comedy         6.8

Top 3 Rated Movies
---------------------------------------------------
The Shining               1980   Thriller / Horror       9.8
The Shawshank Redemption  1994   Drama                   9.7
The Godfather             1972   Crime / Drama           9.2

...

Choose what you would like to sort by (title, year, or rating): year
Ascending or Descending (A or D)? d

Reverse sorted by year
---------------------------------------------------
The Wild Robot            2024   Action / Comedy         6.8
Inception                 2010   Sci-fi / Thriller       8.6
The Dark Knight           2008   Action / Crime / Drama  9.0
The Shawshank Redemption  1994   Drama                   9.7
Pulp Fiction              1994   Crime / Drama           6.5
The Shining               1980   Thriller / Horror       9.8
The Godfather             1972   Crime / Drama           9.2

INTERMEDIATE
Which genre would you like to filter by? drama

Filtered by Drama
---------------------------------------------------
The Godfather             1972   Crime / Drama           9.2
The Shawshank Redemption  1994   Drama                   9.7
Pulp Fiction              1994   Crime / Drama           6.5
The Dark Knight           2008   Action / Crime / Drama  9.0

... 

Unique Genres: ['Action', 'Adventure', 'Comedy', 'Crime', 'Drama', 'Horror', 'Sci-fi', 'Thriller']
Which genre would you like to filter by? war

No movies match your filter.

... 

YES or NO, would you like to update a movie's rating? yes
Which movie's rating would you like to update? the shining
What is the new rating? 9.7
The Shining rating successfully updated.

...

YES or NO, would you like to update a movie's rating? yes
Which movie's rating would you like to update? Star Wars
What is the new rating? 8.0
Error: Movie not found

...

===== Genre Statistics =====
Genre             Avg Rating    Count
--------------------------------------
Horror                  9.80        1
Thriller                9.20        2
Action                  9.00        1
Drama                   8.60        4
Sci-fi                  8.60        1
Crime                   8.23        3
Adventure               6.80        1
Comedy                  6.80        1

...

Choose what you would like to sort by (title, year, or rating): year
Ascending or Descending (A or D)? d

Reverse sorted by year
---------------------------------------------------
The Wild Robot            2024   Adventure / Comedy      6.8
Inception                 2010   Sci-fi / Thriller       8.6
The Dark Knight           2008   Action / Crime / Drama  9.0
The Shawshank Redemption  1994   Drama                   9.7
Pulp Fiction              1994   Crime / Drama           6.5
The Shining               1980   Thriller / Horror       9.8
The Godfather             1972   Crime / Drama           9.2
'''
#takes user inputs and creates a dictionary 
def create_movie(title, year, genres, rating):
    movie_dict = {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating
    }
    return movie_dict

#displays movies heading dependent via keyword arguments in __main__ in a formatted table
def display_movies(movies, heading):
    print(f"\n{heading}")
    print("---------------------------------------------------")
    if len(movies) > 0:
        for movie in movies:
            genres_str = " / ".join(movie["genres"])
            print(f"{movie['title']:<25} {movie['year']:<6} {genres_str:<22} {movie['rating']:>4}")
    else:
        print("No movies in this collection")

#find the top n rated movies by sorting the list of dictionaries by movie rating and slicing the sorted list at n movies
def find_top_rated(movies, n):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    top_n_movies = sorted_movies[:n]    
    return top_n_movies

#uses a counter to help get the average rating of the movies 
def get_average_rating(movies):
    ratings = 0
    for movie in movies:
        ratings += movie["rating"]
    return round(ratings/len(movies), 2)

#Intermediate
#filters movies by genre
def filter_by_genre(movies, genre):
    genre_sorted = []
    for movie in movies:
        if genre.lower() in [g.lower() for g in movie["genres"]]:
            genre_sorted.append(movie)
    return genre_sorted

#updates a movie's rating based on user input new_rating
def update_rating(movies, title, new_rating):
    for movie in movies:
        if title.lower() == movie["title"].lower():
            movie["rating"] = new_rating
            return True
    return False

#makes a list of unique genres, averages the rating of each movie dependent on their genre, & initializes a list where tuples of the genre stats get appended
def get_genre_stats(movies):
    tuple_list = []
    unique_genres_list = []
    for movie in movies:
        for genre in movie["genres"]:
            if genre not in unique_genres_list:
                unique_genres_list.append(genre)

    for genre in unique_genres_list:
        genre_combined_ratings = 0
        count = 0
        for movie in movies:
            if genre in movie["genres"]:
                genre_combined_ratings += movie["rating"]
                count += 1

        genre_avg_rating = round(genre_combined_ratings / count, 2)
        genre_tuple = (genre, genre_avg_rating, count)
        tuple_list.append(genre_tuple)

    tuple_list.sort(key=lambda x: x[1], reverse=True)
    return tuple_list

#sorts movies by user input
def sort_movies(movies, sort_key, reverse=False):
    sort_options = ["title", "year", "rating"]
    sort_key = sort_key.lower()
    if sort_key in sort_options:
        return sorted(movies, key=lambda m: m[sort_key], reverse=reverse)
    else:
        return movies

if __name__ == "__main__":
    #initializes list of dictionaries with movie information
    movies = [
        {
            "title": "Inception",
            "year": 2010,
            "genres": ["Sci-fi", "Thriller"],
            "rating": 8.6
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama"],
            "rating": 9.7
        },
        {
            "title": "The Godfather",
            "year": 1972,
            "genres": ["Crime", "Drama"],
            "rating": 9.2
        },
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genres": ["Action", "Crime", "Drama"],
            "rating": 9.0
        },
        {
            "title": "Pulp Fiction",
            "year": 1994,
            "genres": ["Crime", "Drama"],
            "rating": 6.5
        }
        ]

    #display collection
    display_movies(movies, heading="Your Movie Collection")

    #ask user to add 2 new movies
    print("\nYou will now enter two new movies.")
    for _ in range(2):
        title = input("\nEnter movie title: ")
        year = int(input("Enter movie year: "))
        
        genres_input = input("Enter genres (separated by commas): ")
        genres = [genre.strip().title() for genre in genres_input.split(",")]
        
        rating = float(input("Enter movie rating: "))
        
        movie_dict = create_movie(title.title(), year, genres, rating)
        movies.append(movie_dict)

    #sort movies then display() sorted list by year of release
    movies.sort(key=lambda m: m["year"])
    display_movies(movies, heading="All Movies Sorted by Year")

    #call find_top_rated(movies, 3) and display_movies() with top 3 ratings
    display_movies(find_top_rated(movies, 3), heading="Top 3 Rated Movies")

    #call get_average_rating() and print result as a labeled line such as Collection average rating: number
    print(f"\nCollection average rating: {get_average_rating(movies)}")

    #INTERMEDIATE
    #display all unique genres found as a sorted list. do this by looping through the movies collection and checking each genre 
        #do not call get_genre_stats() for this step
    unique_genres = []
    for movie in movies: 
        for genre in movie["genres"]:
            if genre not in unique_genres:
                unique_genres.append(genre)
    unique_genres.sort()
    print(f"Unique Genres: {unique_genres}")

    #ask the user to enter a genre to filter by. call filter_by_genre() and displat results using display_movies()
        #if no results found, print a message to indicate that no movies match
    genre_filter = input("Which genre would you like to filter by? ").title()
    if genre_filter in unique_genres:
        display_movies(filter_by_genre(movies, genre_filter), heading=f"Filtered by {genre_filter}")
    else:
        print("\nNo movies match your filter.")

    #ask the user if they want to update a rating. if yes, prompt for the new movies title and rating. call update_rating()
        #and print a success or not-found message based on its return value. re-display the collection after a successful update
    decision = input("\nYES or NO, would you like to update a movie's rating? ")
    if decision.lower() == "yes":
        movie_to_update = input("Which movie's rating would you like to update? ").title()
        new_rating = float(input("What is the new rating? "))
        if update_rating(movies, movie_to_update, new_rating) == True:
            print(f"{movie_to_update} rating successfully updated.\n")
        else: 
            print("Error: Movie not found\n") 
    else: 
        print()     

    #call get_genre_stats() and display results as a formatted table showing genre, average raitng, and movie count, sorted from highest to lowest average rating
    genre_stats = get_genre_stats(movies)
    print("===== Genre Statistics =====")
    print(f"{'Genre':<15} {'Avg Rating':>12} {'Count':>8}")
    print("-" * 38)
    
    for stat in genre_stats:
        genre, avg_rating, count = stat
        print(f"{genre:<15} {avg_rating:>12.2f} {count:>8}")
        #I THINK IM DONE WITH THIS ONE

    #ask user to choose a sort order: by title, year, or rating and whether it should be in ascending or descending order
        #call sort_movies() with the appropriate arguments and display sorted result
    order_options = ["title", "year", "rating"]
    sort_order = input("\nChoose what you would like to sort by (title, year, or rating): ")
    a_or_d = input("Ascending or Descending (A or D)? ")
    sort_order.title()
    if a_or_d.lower() == "a":
        display_movies(sort_movies(movies, sort_order, reverse=False), heading=f"Sorted by {sort_order}")
    elif a_or_d.lower() == "d":
        display_movies(sort_movies(movies, sort_order, reverse=True), heading=f"Reverse sorted by {sort_order}")