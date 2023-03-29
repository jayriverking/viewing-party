# tester_data
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

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating: 
        return {"title": title, "genre": genre, "rating": rating}
    else: 
        return None



def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    return user_data 


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data



def watch_movie(user_data, title):
    #conditional, remove fromwatchlist go to watch, return user_data 

    # always return user_data 
    # print(user_data["watchlist"][0]["title"])
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i]["title"])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data

    

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


# print(get_available_recs(james_data))


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

# HELPER FUNC1: GET FAVORITE GENRE(user_data):
# new dict to keep count > counter_dict
# fav_genre = ""
# score = 0
# > access movies watched list: genre --> loop;
#  if movie["genre"] not in counter_dict:
# counter_dict[genre] = 1
# else counter_dict[genre] += 1
# > loop through counter_dict; key, val in items()
# > if val > score: fav_genre = key
# return fav genre

def get_favorite_genre(user_data):
    counter_dict = {}
    fav_genre = ""
    score = 0
    for i in range(len(user_data["watched"])):
        genre =  user_data["watched"][i]["genre"]
        if genre not in counter_dict:
            counter_dict[genre] = 1
        else:
            counter_dict[genre] += 1
    # print(counter_dict)
    for genre, counter in counter_dict.items():
        if counter > score:
            score = counter
            fav_genre = genre
    return fav_genre



# HELPER FUNCTION 2: GET FRIENDS WATCHED LIST:
# movies_friends_watched = []
# loop through the user_data list & get to friends list > [i] > loop
# append movies to movies_friends_watched
# return movies_friends_watched

def get_friends_watched_list(user_data):
    movies_friends_watched = []
    friends = user_data["friends"]
    # print(friends)
    for dict in friends:
        watched = dict["watched"]
        # print(watched)
        for movie in watched:
            if movie not in movies_friends_watched:
                movies_friends_watched.append(movie)
    return movies_friends_watched


# Create a function named get_new_rec_by_genre. This function should...
# take one parameter: user_data
# recommended_movies = []
# user_fav_genre = <<<HELPER FUNCTION 1: get_favotire_genre(user_data)>>>
# user_watched = user_data["watched"]
# friends_watched_list =  <<<HELPER FUNCTION>>>
# for movies in friends_watched_list:
# If movie["genre"] == user_fav_genre and movie not in user_watched:
# recommended_movies.append(movie)
# return recommended movies

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    user_fav_genre = get_favorite_genre(user_data)
    user_watched = user_data["watched"]
    print(user_fav_genre)
    # print(user_watched)
    friends_watched = get_friends_watched_list(user_data)
    for movie in friends_watched:
        # print(movie["genre"])
        if movie["genre"] == user_fav_genre and movie not in user_watched:
            recommended_movies.append(movie)
    return recommended_movies



# Create a function named get_rec_from_favorites. This function should...
# take one parameter: user_data
# def get_rec_from_favorites(user_data):
# favorites = user_data["favorites"]
# recommended_by_user = []
# friends_watched = get_Friends_watched lol
# for movie in favorites:
# if movie not in friends_watched:
# recommended_by_user.append(movie) 

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    recommended_by_user = []
    friends_watched = get_friends_watched_list(user_data)
    for movie in favorites:
        if movie not in friends_watched and movie not in recommended_by_user:
            recommended_by_user.append(movie)
    return recommended_by_user


