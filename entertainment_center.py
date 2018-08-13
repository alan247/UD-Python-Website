import fresh_tomatoes

import media

toy_story = media.Movie(
    "Toy Story",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "http://youtu.be/vwyZH85NQC4"
)

avatar = media.Movie(
    "Avatar",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://youtu.be/-9ceBgWV8io"
)

school_of_rock = media.Movie(
    "School of Rock",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "http://youtu.be/3PsUJFEBC74"
)

locke = media.Movie(
    "Locke",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1MjE5MzU2M15BMl5BanBnXkFtZTgwNzE4OTMzMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://youtu.be/MyoO35P41YM"
)

lucy = media.Movie(
    "Lucy",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://youtu.be/2tI7w1ffWrs"
)

all_is_lost = media.Movie(
    "All Is Lost",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI0MzIyMjU1N15BMl5BanBnXkFtZTgwOTk1MjQxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://youtu.be/no1rl9Gvx-s"
)

american_beauty = media.Movie(
    "American Beauty",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM4NTI5NzYyNV5BMl5BanBnXkFtZTgwNTkxNTYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://youtu.be/3ycmmJ6rxA8"
)

cafe_de_flore = media.Movie(
    "Cafe de Flore",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgyOTExNzM1Ml5BMl5BanBnXkFtZTcwMDExMzY2Ng@@._V1_UY268_CR2,0,182,268_AL_.jpg",  # noqa
    "https://youtu.be/2mZYl9srG0M"
)

split = media.Movie(
    "Split",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZTJiNGM2NjItNDRiYy00ZjY0LTgwNTItZDBmZGRlODQ4YThkL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://youtu.be/6bfooooTKyM"
)

movies = [
    toy_story,
    avatar,
    school_of_rock,
    locke,
    lucy,
    all_is_lost,
    american_beauty,
    cafe_de_flore,
    split
]

fresh_tomatoes.open_movies_page(movies)
