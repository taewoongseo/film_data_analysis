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


#Running functions
runtime('film_data.db')
