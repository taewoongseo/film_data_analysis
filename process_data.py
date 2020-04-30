#Name: Taewoong Seo

import requests
import json
import sqlite3

print("My Favorite Movies!")

user_input = input('Type in a film title: ')

def request_api(title):

    endpoint = 'http://www.omdbapi.com/'
    parameters = {'apikey': 'ec2e4fa8', 't': title, 'type': 'movie', 'r': 'json'}

    omdb_r = requests.get(url = endpoint, params = parameters)
    omdb_data = omdb_r.json()

    if omdb_data['Response'] == 'False':
        print("Try a valid title!")
        exit()
    else:
        return(omdb_data)

def process_data(movie_d):
    title = movie_d['Title']
    year = int(movie_d['Year'])
    rated = movie_d['Rated']
    runtime = int(movie_d['Runtime'].split(' ')[0])
    genres = movie_d['Genre']
    director = movie_d['Director']
    actors = movie_d['Actors']
    plot = movie_d['Plot']
    country = movie_d['Country']
    imdb_rating = float(movie_d['imdbRating'])

    conn = sqlite3.connect('film_data.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Films (title TEXT, year INTEGER, rated TEXT, runtime INTEGER, genres TEXT, director TEXT, actors TEXT, plot TEXT, country TEXT, imdb_rating REAL)')
    cur.execute('SELECT * FROM Films WHERE title = ?', (user_input, ))
    if not cur.fetchone():
        cur.execute('INSERT OR IGNORE INTO Films (title, year, rated, runtime, genres, director, actors, plot, country, imdb_rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (title, year, rated, runtime, genres, director, actors, plot, country, imdb_rating))
        conn.commit()
    else:
        print("Please type in a new title")
        exit()
    


new_d = request_api(user_input)
process_data(new_d)


