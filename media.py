class Movie():
    """ Movie instance constructor. Each instance has a title,
    poster and youtube trailer url

    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
