def movie_organizer(*args):
    collection = {}

    result = ""
    for movie_name, genre in args:
        if genre not in collection:
            collection[genre] = []
        collection[genre].append(movie_name)

    sorted_movie_collection = sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for genre, movies in sorted_movie_collection:
        result += f"{genre} - {len(movies)} \n"
        for movie in movies:
            result += f"* {movie}\n"
    return result

print(movie_organizer(

("The Godfather", "Drama"),

("The Hangover", "Comedy"),

("The Shawshank Redemption",

"Drama"),

("The Pursuit of Happiness",

"Drama"),

("The Hangover Part II", "Comedy")))