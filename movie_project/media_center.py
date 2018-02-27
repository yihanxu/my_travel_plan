# media center
import fresh_tomatoes
import media
import turtle

toy_story = media.Movie("Toy Story 1", 
						"A story of a boy and his toys", 
						"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar", 
						"A marine on an alienn planet", 
						"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", 
						"https://www.youtube.com/watch?v=6ziBFh3V1aM")

shadowlands = media.Movie("Shadowlands",
							"How the Oxford don C.S. Lewis (Jack) met Joy, his wife",
							"https://static.rogerebert.com/uploads/movie/movie_poster/shadowlands-1994/large_5t1Y8L1jyiendX4uHHqeom7AlWi.jpg",
							"https://www.youtube.com/watch?v=NLKS0XGRYi8")

# print(toy_story.title)
# print(toy_story.storyline)
# print(avatar.title)
# print(avatar.storyline)
# avatar.show_trailer()
# print(shadowlands.title)
# print(shadowlands.storyline)
# shadowlands.show_trailer()

# # create movie lists
# movies = [toy_story, avatar, shadowlands]
# fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print (turtle.Turtle.__doc__)
print (media.Movie.__doc__)