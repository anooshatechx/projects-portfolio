# 🎯 Smart Recommendation: Book & Movie Explorer
import json
import requests

while True:
    user = input("""What would you like to explore?
1. Book 📕
2. Movie 🍿
Answer: """)

    if user.strip().lower() in ["1", "book"]:
        choice = input("Enter the book title 📖: ").strip().lower()
        link = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": choice}
        extract = requests.get(link, params=params)
        data = extract.json()

        if "items" not in data or len(data["items"]) == 0:
            print("No book found. Try again!")
            continue

        book = data["items"][0]["volumeInfo"]
        title = book.get("title", "No Title")
        author = book.get("authors", ["Unknown Author"])
        date = book.get("publishedDate", "No info")
        des = book.get("description", "No description available")
        genre = book.get("categories", ["No info"])
        rating = book.get("averageRating", "No Rating")
        rating_count = book.get("ratingsCount", 0)
        pages = book.get("pageCount", "No info")

        print("\n----------------📖 BOOK INFO 📖----------------")
        print("Title:", title)
        print("Author:", ", ".join(author))
        print("Published Date:", date)
        print("Genre:", ", ".join(genre))
        print("Ratings:", rating)
        print("Rating Count:", rating_count)
        print("Pages:", pages)
        print("Description:", des)
        print("-------------------------------------------\n")

    elif user.strip().lower() in ["2", "movie"]:
        user2 = input("Enter the movie name 🍿: ").strip()
        link2 = "http://www.omdbapi.com/"
        params = {"t": user2, "apikey": "c5f5bb57"}
        get = requests.get(link2, params=params)
        y = get.json()

        if y.get("Response") == "False":
            print("Movie not found! Try again.")
            continue

        title = y.get("Title", "No info")
        released = y.get("Released", "No info")
        country = y.get("Country", "No info")
        runtime = y.get("Runtime", "No info")
        genre = y.get("Genre", "No info")
        
        if y.get("Ratings") and len(y["Ratings"]) > 0:
            rating = y["Ratings"][0]["Value"]
        else:
            rating = "No Rating"

        plot = y.get("Plot", "No description available")

        print("\n----------------🍿 MOVIE INFO 🍿----------------")
        print("Title:", title)
        print("Released:", released)
        print("Country:", country)
        print("Watch time:", runtime)
        print("Genre:", genre)
        print("Ratings:", rating)
        print("Plot:", plot)
        print("--------------------------------------------\n")

    else:
        print("Invalid choice! Please enter 1 or 2.")
        continue

    again = input("Another Book/Movie? y/n: ")
    if again.strip().lower() not in ["yes", "y"]:
        print("Bye! See ya soon 💗")
        break
    else:
    	print("Yayyy! Lets go 🤝")
