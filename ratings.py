
def ratings_dict_maker(filename):
    """Restaurant rating lister."""
    #Open file
    rest_scores = open(filename)

    #Create empty dictionary
    rest_ratings = {}

    #Restaurant name is key, rating is value
    #Oh my gosh they are all restaurant names from Harry Potter!

    #Fill dictionary first
    for line in rest_scores:
        restaurants = line.split(":")
        for restaurant in restaurants:
            rest_ratings[restaurant] = rest_ratings.get(restaurant, 0) + 1

    #Close file
    rest_scores.close()
    #Return dictionary
    return rest_ratings

    def ratings_finder(dictionary):
    #Going to try to split this into a separate function
    #Use dict.items() to list dictionary items
        
        for restaurants, rating in rest_ratings.values():
            print(f"{restaurant}: {rating}")


    
    
    #Use dict.items() to list dictionary items
    # for rest_rating, rating in rest_ratings.items():
    #     print(f"{rest_rating}: {rating}")

print(ratings_dict_maker("scores.txt"))



