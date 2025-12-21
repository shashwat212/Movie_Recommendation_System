from collections import Counter

# Movie Database
movies = [
    {
        "title": "Inception",
        "genre": ["Sci-Fi", "Action", "Thriller"],
        "actor": ["Leonardo DiCaprio"],
        "director": ["Christopher Nolan"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Interstellar",
        "genre": ["Sci-Fi", "Drama"],
        "actor": ["Matthew McConaughey"],
        "director": ["Christopher Nolan"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "The Dark Knight",
        "genre": ["Action", "Drama"],
        "actor": ["Christian Bale"],
        "director": ["Christopher Nolan"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Titanic",
        "genre": ["Romance", "Drama"],
        "actor": ["Leonardo DiCaprio"],
        "director": ["James Cameron"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "The Matrix",
        "genre": ["Sci-Fi", "Action"],
        "actor": ["Keanu Reeves"],
        "director": ["Lana Wachowski"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Forrest Gump",
        "genre": ["Drama", "Romance"],
        "actor": ["Tom Hanks"],
        "director": ["Robert Zemeckis"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Gladiator",
        "genre": ["Action", "Drama"],
        "actor": ["Russell Crowe"],
        "director": ["Ridley Scott"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Avatar",
        "genre": ["Sci-Fi", "Adventure"],
        "actor": ["Sam Worthington"],
        "director": ["James Cameron"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Joker",
        "genre": ["Drama", "Thriller"],
        "actor": ["Joaquin Phoenix"],
        "director": ["Todd Phillips"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "The Revenant",
        "genre": ["Drama", "Adventure"],
        "actor": ["Leonardo DiCaprio"],
        "director": ["Alejandro G. Iñárritu"],
        "awards": ["Oscar Winner"]
    },
    {
        "title": "Dune",
        "genre": ["Sci-Fi", "Adventure"],
        "actor": ["Timothée Chalamet"],
        "director": ["Denis Villeneuve"],
        "awards": ["Oscar Winner"]
    }
]

# Welcome Message
def welcome():
    print("\n🎬 Welcome to the Smart Movie Recommendation System!")
    print("Type a movie name to get recommendations.")
    print("Type 'list' to see available movies.")
    print("Type 'bye' or 'exit' to quit.\n")

# Show available movies
def show_movies():
    print("\n📽️ Available Movies:\n")
    for movie in movies:
        print(f"🎞️ {movie['title']}")
        print(f"   Genre   : {', '.join(movie['genre'])}")
        print(f"   Actor   : {', '.join(movie['actor'])}")
        print(f"   Director: {', '.join(movie['director'])}")
        print(f"   Awards  : {', '.join(movie['awards'])}")
        print("-" * 40)

# Similarity calculation
def calculate_similarity(movie1, movie2):
    score = 0

    score += len(set(movie1["genre"]) & set(movie2["genre"])) * 3
    score += len(set(movie1["actor"]) & set(movie2["actor"])) * 4
    score += len(set(movie1["director"]) & set(movie2["director"])) * 5
    score += len(set(movie1["awards"]) & set(movie2["awards"])) * 2

    return score

# Recommendation logic
def recommend(movie_name):
    selected_movie = None

    for movie in movies:
        if movie["title"].lower() == movie_name.lower():
            selected_movie = movie
            break

    if not selected_movie:
        print("\n❌ Movie not found. Please check the available movie list.\n")
        return

    scores = []

    for movie in movies:
        if movie != selected_movie:
            similarity = calculate_similarity(selected_movie, movie)
            scores.append((movie, similarity))

    scores.sort(key=lambda x: x[1], reverse=True)

    print(f"\n🎯 Top Movie Recommendations for '{selected_movie['title']}':\n")

    for idx, (movie, score) in enumerate(scores[:10], start=1):
        print(f"{idx}. 🎬 {movie['title']}")
        print(f"   Genre   : {', '.join(movie['genre'])}")
        print(f"   Actor   : {', '.join(movie['actor'])}")
        print(f"   Director: {', '.join(movie['director'])}")
        print(f"   Awards  : {', '.join(movie['awards'])}")
        print("-" * 40)

# Main Program Loop
def main():
    welcome()

    while True:
        user_input = input("👉 Enter movie name: ").strip()

        if user_input.lower() in ["bye", "exit"]:
            print("\n👋 Thank you for using the Movie Recommendation System. Enjoy watching!\n")
            break

        elif user_input.lower() == "list":
            show_movies()

        else:
            recommend(user_input)

# Run Program
main()
