import fresh_tomatoes
import media

shrek = media.Movie('Shrek',
                        'An anti fairy tale',
                        'https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg',
                        'http:www.youtube.com/watch?v=jYejzdBwvY4')

ex_machina = media.Movie('Ex Machina',
                         'A tech employee is flown to a remote location to perform the ultimate Turing test.',
                         'https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg',
                         'http://www.youtube.com/watch?v=XYGzRB4Pnq8')

this_is_40 = media.Movie('This is 40',
                         'getting older is fun to watch, not always fun to live',
                         'https://upload.wikimedia.org/wikipedia/en/e/eb/This_is_40.jpg',
                         'http://www.youtube.com/watch?v=5qLlDRyWKm4')

the_rocker = media.Movie('The Rocker',
                         'An old washed up rocker comes back to his love of playing in a band.',
                         'https://upload.wikimedia.org/wikipedia/en/d/d7/Rockerposter.jpg',
                         'www.youtube.com/watch?v=CqWUXIfj2VM')

braveheart = media.Movie('Braveheart',
                         'The story of William Wallace',
                         'https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg',
                         'http://www.youtube.com/watch?v=wj0I8xVTV18')

lord_of_the_rings_1 = media.Movie('The Lord of the Rings: The Fellowship of the Ring',
                         'The first chapter of the epic fantasy war with the ultimate evil.',
                         'https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg',
                         'http://www.youtube.com/watch?v=V75dMMIW2B4')

movies = [shrek, ex_machina, this_is_40, the_rocker, braveheart, lord_of_the_rings_1]
fresh_tomatoes.open_movies_page(movies)



