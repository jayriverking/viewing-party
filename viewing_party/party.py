# james_data (= amandas_data)
# james_data = {
#     "watched": [
#         {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# }, 
#         {
#     "title": "The Lord of the Functions: The Two Parameters",
#     "genre": "Fantasy",
#     "rating": 4.0
# }, 
#         {
#     "title": "The Lord of the Functions: The Return of the Value",
#     "genre": "Fantasy",
#     "rating": 4.0
# }, 
#         {
#     "title": "The JavaScript and the React",
#     "genre": "Action",
#     "rating": 2.2
# }, 
#         {
#     "title": "Recursion",
#     "genre": "Intrigue",
#     "rating": 2.0
# }, 
#         {
#     "title": "Instructor Student TA Manager",
#     "genre": "Intrigue",
#     "rating": 4.5
# }
#         ],    
#     "friends": [
#         {
#             "watched": [
#                 {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# },
#                 {
#     "title": "The Lord of the Functions: The Return of the Value",
#     "genre": "Fantasy",
#     "rating": 4.0
# },
#                 {
#     "title": "The Programmer: An Unexpected Stack Trace",
#     "genre": "Fantasy",
#     "rating": 4.0
# },
#                 {
#     "title": "It Came from the Stack Trace",
#     "genre": "Horror",
#     "rating": 3.5
# },
#             ]
#         },
#         {
#             "watched": [
#                 {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# },
#                 {
#     "title": "The JavaScript and the React",
#     "genre": "Action",
#     "rating": 2.2
# },
#                 {
#     "title": "Recursion",
#     "genre": "Intrigue",
#     "rating": 2.0
# },
#                 {
#     "title": "Zero Dark Python",
#     "genre": "Intrigue",
#     "rating": 3.0
# },
#             ]
#         }
#     ]  

# }
james_data = {
  "subscriptions": ['hulu', 'netflix','amazon', 'disney+'],
    "watched": [
        {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}, 
        {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}, 
        {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}, 
        {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}, 
        {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}, 
        {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
        ],    
    "friends": [
        {
            "watched": [
                {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8,
    "host": 'disney+'
},
                {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0,
                  "host": 'hulu'
},
                {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0,
                  "host": 'the wrong host'
},
                {
    "title": "It Came from the Stack Trace",
    "genre": "Horror",
    "rating": 3.5,
                  "host": 'amazon'
},
            ]
        },
        {
            "watched": [
                {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8,
                  "host": 'the wrong host'
},
                {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2,
                  "host": 'netflix'
},
                {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0,
                  "host": 'the wrong host'
},
                {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0,
                  "host": 'disney+'
},
            ]
        }
    ]  

}


# tester data
# janes_data = {
#         "watchlist": [{
#             "title": "MOVIE_TITLE_1",
#             "genre": "GENRE_1",
#             "rating": 1
#         }],
#         "watched": [{
#             "title": "MOVIE_TITLE_2",
#             "genre": "GENRE_2",
#             "rating": 2
#         }, {
#             "title": "MOVIE_TITLE_1",
#             "genre": "GENRE_1",
#             "rating": 1
#         }, {
#             "title": "MOVIE_TITLE_3",
#             "genre": "GENRE_3",
#             "rating": 3
#         }, 
#         {
#             "title": "MOVIE_TITLE_4",
#             "genre": "GENRE_3",
#             "rating": 2
#         }],
#     "friends": [{"watched": [{
#             "title": "MOVIE_TITLE_5",
#             "genre": "GENRE_1",
#             "rating": 1
#         }, {
#             "title": "MOVIE_TITLE_2",
#             "genre": "GENRE_2",
#             "rating": 2
#         }, {
#             "title": "MOVIE_TITLE_3",
#             "genre": "GENRE_3",
#             "rating": 3
#         }, 
#         {
#             "title": "MOVIE_TITLE_8",
#             "genre": "GENRE_3",
#             "rating": 2
#         }]}]
#     }




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
    # if watchlist is empty , return zero
    if len(user_data['watched']) == 0:
        return 0
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

# print(get_watched_avg_rating(janes_data))

    # take one parameter: user_data
    #     the value of user_data will be a dictionary with a "watched" list of movie dictionaries
    #         This represents that the user has a list of watched movies
    # Calculate the average rating of all movies in the watched list
    #     The average rating of an empty watched list is 0.0
    # return the average rating

# Function 2 

    # Create a function named get_most_watched_genre. This function should...
def get_most_watched_genre(user_data):
    counter = {}
    most_genre = ""
    score = 0 
    if len(user_data['watched']) == 0:
        return None
    for dict in user_data["watched"]:
        # print(dict['genre'])
        if dict['genre'] not in counter:
            counter[dict['genre']] = 1
        else:
            counter[dict['genre']] += 1
    # print(counter)
    for key, values in counter.items():
        # print(values)
        if values >= score:
            score = values
            most_genre = key
    return most_genre


# print(get_most_watched_genre(janes_data))

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

def get_unique_watched(user_data):
    friends_list = []
    user_list = []
    diff_list = []# (if dict in user_list and dict not in friends_list, append dict to diff list) = []

    # loop through user_data 
    for i in range(len(user_data["watched"])): #for i in range(len(user_data['watched_list'])):
        # print(i)
        user_list.append(user_data["watched"][i])# user_data [watched list][i] # > append dicts to user_list
        # print(user_list)
    for j in range(len(user_data["friends"])):
        for dict in (user_data["friends"][j]["watched"]):
            friends_list.append(dict)
    # print(friends_list)
    # print(f"{user_list=}, {friends_list=}")
    for dict in user_list: 
        # print(dict)
        if dict not in friends_list:
            diff_list.append(dict)
    # print(f"USER_LIST: {user_list}, FRIENDS_LIST: {friends_list}")
    return diff_list
        
# print(get_unique_watched(james_data)) 
        
    # 2nd loop through user_data [friends] [friends watched list][i] > append dicts to friends_list
    # for dict in user_list if dict not in friends_list > append dict to diff list
    # return diff list

# function 1 
# Create a function named get_unique_watched. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# This represents that the user has a list of watched movies and a list of friends
# The value of "friends" is a list "friends": [{"watched": []}]
# Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
# Each movie dictionary has a "title".
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies


# def get_friends_unique_watched(user_data):
# same logic as above, just reversed lol
def get_friends_unique_watched(user_data):
    friends_list = []
    user_list = []
    diff_list = []# (if dict in user_list and dict not in friends_list, append dict to diff list) = []

    # loop through user_data 
    for i in range(len(user_data["watched"])): #for i in range(len(user_data['watched_list'])):
        # print(i)
        user_list.append(user_data["watched"][i])# user_data [watched list][i] # > append dicts to user_list
        # print(user_list)
    for j in range(len(user_data["friends"])):
        for dict in (user_data["friends"][j]["watched"]):
            friends_list.append(dict)
    # print(friends_list)
    # print(f"{user_list=}, {friends_list=}")
    for dict in friends_list: 
        # print(dict)
        if dict not in user_list and dict not in diff_list:
            diff_list.append(dict)
    # print(f"USER_LIST: {user_list}, FRIENDS_LIST: {friends_list}")
    return diff_list
        
# print(get_friends_unique_watched(james_data)) 

# function 2
# Create a function named get_friends_unique_watched. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# This represents that the user has a list of watched movies and a list of friends
# The value of "friends" is a list
# Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
# Each movie dictionary has a "title".
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# Return a list of dictionaries, that represents a list of movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    reccomendation_list = []
    shared_sub = []

    # Create a function named get_available_recs. This function should...
#___________________________________________________



    # for host in (user_data["subscriptions"]):
    #     print(host)

    # 
    for sub in (user_data["friends"][0]["watched"]): # iterating through user_data's friend key indexing to the watched key 
        # print(sub)
        # 
        if sub['host'] in user_data["subscriptions"]: # this is accessing the data in side the sub["host"] category  and it's checkint to see if the same data is in user_data's subscriptions 
            # print(sub["host"])
            shared_sub.append(sub['host']) # this is appending those subscriptions to the share_sub list. 
            # print(shared_sub)
   
    for dict in (user_data["friends"][0]["watched"]):
        # print(dict["title"])
        if dict["title"] not in user_data["watched"][0]["title"]:
                
            # possible step checking common hosts. 
            reccomendation_list.append(dict["title"])
            print(reccomendation_list)

    return reccomendation_list
        #  Determine a list of recommended movies. A movie should be added to this list if and only if:
    #     The user has not watched it
    #     At least one of the user's friends has watched
    #     The "host" of the movie is a service that is in the user's "subscriptions"
    # Return the list of recommended movies
    
        # if movie in firends watched and not in user watched and in shared_sub 
    # add to reccomendations. 
        
        # if sub['host'] in user_data["friends"][0]["watched"]:   
        #     print(sub)     
        #     #
            # # NOW WE KNOW WHAT SUB IS :>
            # print(shared_sub)
        
        # FOR TRYING OUT PURPOSES; WHY AM I IN ALL CAPS 
        
        
       
        #     shared_sub.append
        #     print(shared_sub)
    
   
    

    
   
        
        # if host in user_data["subscriptions"] and host in user_data["friends"]:
        #     shared_sub.append(host)
        #     print(shared_sub)
    
 

#     for movie in user_data["subcriptions"]:
#         if movie in user_data["friends"]["watched"] and movie not in user_data["watched"]:
#             reccomendation_list.append
print(get_available_recs(james_data))
# should we make helper function from 
# for friend in friends, get watched , 
# # get watched movies 
# if host in movie and host_ in user data 
    # the host in the movie list and it's in user dats host 

# if movie in friends and no in user_data. 
#     reccomendation.append(movie)
    
#     return movies 


    #-----------------__________
    # take one parameteruser_data
    #     user_data will have a field "subscriptions". The value of "subscriptions" is a list of strings
#         This represents the names of streaming services that the user has access to
#         Each friend in "friends" has a watched list. Each movie in the watched list has a "host", 
# which is a string that says what streaming service it's hosted on
    #


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Create a function named get_new_rec_by_genre. This function should...
# take one parameter: user_data
# def get_new_rec_by_genre(user_data)
# Consider the user's most frequently watched genre. Then, determine a list of recommended movies. 
# A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies
# Create a function named get_rec_from_favorites. This function should...
# take one parameter: user_data
# user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
# This represents the user's favorite movies
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The movie is in the user's "favorites"
# None of the user's friends have watched it
# Return the list of recommended movies