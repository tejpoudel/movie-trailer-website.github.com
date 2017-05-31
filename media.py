import webbrowser #Import webbrowser to open the browser. 

class Favorite_Movies():
    #define init function.
    def __init__(self, movie_title, movie_description, poster_url, youtube_url):
        self.title = movie_title 
        self.storyline = movie_description
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url

    #define show_gtrailer function to show the movie trailer in webbrowser.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
