# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating: 
        return {"title": title, "genre": genre, "rating": rating}
    else: 
        return None
# If those three attributes are truthy, then return a dictionary. This dictionary should...
# Have three key-value pairs, with specific keys
# The three keys should be "title", "genre", and "rating"
# The values of these key-value pairs should be appropriate values
# If title is falsy, genre is falsy, or rating is falsy, this function should return None

def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    return user_data 

# function 2:
# Create a function named add_to_watched. This function should...
# take two parameters: user_data, movie
# the value of user_data will be a dictionary with a key "watched", and a value which is a list of dictionaries representing the movies the user has watched
# An empty list represents that the user has no movies in their watched list
# the value of movie will be a dictionary in this format:
# {
#   "title": "Title A",
#   "genre": "Horror",
#   "rating": 3.5
# }
# add the movie to the "watched" list inside of user_data
# return the user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# function 3
# Create a function named add_to_watchlist. This function should...
# take two parameters: user_data, movie
# the value of user_data will be a dictionary with a key "watchlist", and a value which is a list of dictionaries representing the movies the user wants to watch
# An empty list represents that the user has no movies in their watchlist
# the value of movie will be a dictionary in this format:
# {
#   "title": "Title A",
#   "genre": "Horror",
#   "rating": 3.5
# }
# add the movie to the "watchlist" list inside of user_data
# return the user_data


# tester data
janes_data = {
        "watchlist": [{
            "title": "MOVIE_TITLE_1",
            "genre": "GENRE_1",
            "rating": 1
        }],
        "watched": [{
            "title": "MOVIE_TITLE_1",
            "genre": "GENRE_1",
            "rating": 1
        }, {
            "title": "MOVIE_TITLE_2",
            "genre": "GENRE_2",
            "rating": 2
        }, {
            "title": "MOVIE_TITLE_3",
            "genre": "GENRE_3",
            "rating": 3
        }]
    }

def watch_movie(user_data, title):
    #conditional, remove fromwatchlist go to watch, return user_data 

    # always return user_data 
    # print(user_data["watchlist"][0]["title"])
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i]["title"])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data

    





# function 4
# Create a function named watch_movie. This function should...
# take two parameters: user_data, title
# the value of user_data will be a dictionary with a "watchlist" and a "watched"
# This represents that the user has a watchlist and a list of watched movies
# the value of title will be a string
# This represents the title of the movie the user has watched
# If the title is in a movie in the user's watchlist:
# remove that movie from the watchlist
# add that movie to watched
# return the user_data
# If the title is not a movie in the user's watchlist:
# return the user_data
# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

    #Function 1 
    # Create a function named get_watched_avg_rating. This function should...
def get_watched_avg_rating(user_data):
    avg_total = 0
    counter = 0
    # print(user_data["watched"][0]['rating'])
    for dict in user_data["watched"]:
        # print(dict['rating'])
        avg_total += dict['rating']
        counter += 1
    avg_rating = avg_total / counter
    return avg_rating
        # print(sum(dict['rating']))

print(get_watched_avg_rating(janes_data))
    # take one parameter: user_data
    #     the value of user_data will be a dictionary with a "watched" list of movie dictionaries
    #         This represents that the user has a list of watched movies
    # Calculate the average rating of all movies in the watched list
    #     The average rating of an empty watched list is 0.0
    # return the average rating

# Function 2 

    # Create a function named get_most_watched_genre. This function should...

    # take one parameter: user_data
    #     the value of user_data will be a dictionary with a "watched" list of movie dictionaries. Each movie dictionary has a key "genre".
    #         This represents that the user has a list of watched movies. Each watched movie has a genre.
    #         The values of "genre" is a string.
    # Determine which genre is most frequently occurring in the watched list
    # return the genre that is the most frequently watched
    # If the value of "watched" is an empty list, get_most_watched_genre should return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

