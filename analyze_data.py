#calculations and visuals

import sqlite3
import json
import os
import csv
import numpy as np
import matplotlib.pyplot as plt

#Year analysis
def year(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.year FROM Films')
    rows = cur.fetchall()
    
    year_lst = []
    for row in rows:
        year_lst.append(row[0])

    year_d = {}
    for yr in year_lst:
        decade = str(yr)[:3] + '0s'
        if decade not in year_d.keys():
            year_d[decade] = 1
        else:
            year_d[decade] += 1

    sorted_year_d = sorted(year_d, key = lambda k: year_d[k], reverse = True)
    print('You seem to like films from the ' + sorted_year_d[0] + ' the most!')

    return sorted_year_d


#Runtime analysis
def runtime(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.runtime FROM Films')
    rows = cur.fetchall()
    count = 0
    for row in rows:
        count += row[0]
    
    runtime_avg = round(count/len(rows), 2)
    print('Average Runtime: ' + str(runtime_avg) + ' minutes')

    #Visuals
    runtime_lst = []
    for row in rows:
        runtime_lst.append(row[0])

    num_bins = 10
    plt.hist(runtime_lst, num_bins, facecolor='blue', alpha=0.5, rwidth=0.85)
    plt.xlabel('Runtime in Minutes',fontsize=10)
    plt.ylabel('Count',fontsize=10)
    plt.title('Runtime Distribution',fontsize=12)

    plt.show()

    return runtime_avg

#director analysis
def director(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.director FROM Films')
    rows = cur.fetchall()
    director_d = {}

    for row in rows:
        directors = row[0].split(', ')
        for director in directors:
            if director not in director_d.keys():
                director_d[director] = 1
            else:
                director_d[director] += 1

    sorted_director_tup = sorted(director_d.items(), key = lambda k: k[1], reverse = True)

    if sorted_director_tup[0][1] == 1:
        print("You like a wide variety of directors! We need more data to determine your favorite director.") 
        exit()
    else:
        print("Your favorite director is " + sorted_director_tup[0][0] + ". They made " + str(sorted_director_tup[0][1]) + " of your favorite movies!")    
        return sorted_director_tup[0][0]

#actor analysis
def actors(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.actors FROM Films')
    rows = cur.fetchall()
    actor_d = {}

    for row in rows:
        actors = row[0].split(', ')
        for actor in actors:
            if actor not in actor_d.keys():
                actor_d[actor] = 1
            else:
                actor_d[actor] += 1

    sorted_actor_tup = sorted(actor_d.items(), key = lambda k: k[1], reverse = True)

    if sorted_actor_tup[0][1] == 1:
        print("You like a wide variety of actors! We need more data to determine your favorite actors.") 
        exit()
    else:
        print("Your favorite actor is " + sorted_actor_tup[0][0] + ". They appeared in " + str(sorted_actor_tup[0][1]) + " of your favorite movies!")    
        return sorted_actor_tup[0][0]

#genre_analysis
def genres(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.genres FROM Films')
    rows = cur.fetchall()
    genre_d = {}
    for row in rows:
        genres = row[0].split(', ')
        for genre in genres:
            if genre not in genre_d.keys():
                genre_d[genre] = 1 
            else:
                genre_d[genre] += 1
    print(genre_d)

    sorted_genre_d = sorted(genre_d, key = lambda k: genre_d[k], reverse = True)
    print(sorted_genre_d[:3])

def plot(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.plot FROM Films')
    rows = cur.fetchall()

    keyword_d = {}
    for row in rows:
        sentence = row[0]
        keywords = sentence.split(" ")
        for keyword in keywords:
            keyword = keyword.strip(" ,.'")
            if keyword not in keyword_d.keys():
                keyword_d[keyword] = 1
            else:
                keyword_d[keyword] += 1
    sorted_keyword_tup = sorted(keyword_d.items(), key = lambda k: k[1], reverse = True)
    print(sorted_keyword_tup)
    return sorted_keyword_tup


def imdb_rating(filename):
    conn = sqlite3.connect(filename)
    cur = conn.cursor()

    cur.execute('SELECT Films.imdb_rating FROM Films')
    rows = cur.fetchall()
    
    tot = 0
    for row in rows:
        tot += row[0]

    count = len(rows)
    avg_rating = round((float(tot)/count), 1)
    print("Your average film rating from IMDb is " + str(avg_rating))

    rating_lst = []
    for row in rows:
        rating_lst.append(row[0])

    num_bins = 10
    plt.hist(rating_lst, num_bins, facecolor='red', alpha=0.5, rwidth=0.85)
    plt.xlabel('IMDb Rating out of 10',fontsize=10)
    plt.ylabel('Count',fontsize=10)
    plt.title('IMDb Rating Distribution',fontsize=12)

    plt.show()
    
    return avg_rating

#Running functions
#year, runtime, director, actors, genres, plot, imdb_rating
imdb_rating('film_data.db')
