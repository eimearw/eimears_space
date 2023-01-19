current_movies = {'Inception':'11:00am',
                  'Clueless':'1:00pm',
                  'Twilight':'5:00pm',
                  'The Holiday':'8:00pm'}

print("We are currently showing the following movies:")
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("The movie you chose is not playing today :(")
else:
    print(movie, 'is playing at', showtime)

