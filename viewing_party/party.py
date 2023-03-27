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
        "watched": []
    }

def watch_movie(user_data, title):
    #conditional, remove fromwatchlist go to watch, return user_data 

    # always return user_data 
    for dict in user_data["watchlist"]:
        # print(i)
        for k in dict:
            if title in k:
                user_data["watched"].append(dict)
                # print(user_data["watched"])
                user_data["watchlist"].remove(dict)
                # print(user_data["watchlist"])
    return user_data

print(watch_movie(janes_data,"MOVIE_TITLE_1"))

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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

