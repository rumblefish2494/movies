import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'http://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     'A marine on an alien Planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'http://www.youtube.com/watch?v=5PSNL1qE6VY')

this_is_40 = media.Movie('This is 40',
                         'getting older is fun to watch, not always fun to live',
                         'https://upload.wikimedia.org/wikipedia/en/e/eb/This_is_40.jpg',
                         'http://www.youtube.com/watch?v=5qLlDRyWKm4')

school_of_rock = media.Movie('School of Rock',
                             'An old rocker teaches school',
                             'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'http://www.youtube.com/watch?v=3PsUJFEBC74')
#school_of_rock.show_trailer()
braveheart = media.Movie('Braveheart',
                         'The story of William Wallace',
                         'https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg',
                         'http://www.youtube.com/watch?v=wj0I8xVTV18')
movies = [toy_story, avatar, this_is_40, school_of_rock, braveheart]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__module__)

