#calculations and visuals

import sqlite3
import json
import os
import csv
import numpy as np
import matplotlib.pyplot as plt



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

runtime('film_data.db')
