import requests

def BestInGenre(genre):

    if not isinstance(genre, str) or not genre:
        raise ValueError("Input genre must be a string and cannot be empty")
    
    url = "https://jsonmock.hackerrank.com/api/tvseries"
    params = {"page": 1}
    best_movie_rating = 0
    best_movie = None

    try:
        initial_response = requests.get(url, params=params)
        initial_response.raise_for_status()
        total_pages = initial_response.json()["total_pages"]

        for page in range(1, total_pages + 1):
            params["page"] = page
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()

                for movie in response.json()["data"]:
                    if genre.lower() in movie["genre"].lower() and (movie["imdb_rating"] > best_movie_rating or (movie["imdb_rating"] == best_movie_rating and movie["name"] < best_movie["name"])):
                        best_movie_rating = movie["imdb_rating"]
                        best_movie = movie

            except requests.exceptions.RequestException as err:
                print(f"Error fetching page {page}: {err}")
                continue 
    except requests.exceptions.RequestException as err:
        print(f"Error fetching initial data: {err}")

    return best_movie["name"] if best_movie else None


print(BestInGenre("Action"))
