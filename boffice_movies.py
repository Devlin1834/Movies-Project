# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 08:06:52 2017

@author: Devlin
"""

import json
import re
import requests
import csv

## We can use the same format as in meta_movies.py, but because its already been filtered through
#  the api once, we don't have to worry about skipped movies. The skipped ones have already been
#  removed from the dataset on the first go-round.

## Also I ran it twice with both Cinemalists - just be sure to comment out the other lines

movies_list = list(csv.reader(open('D:\Files\Psdir\movies\CinemaList1.csv')))
#movies_list = list(csv.reader(open('D:\Files\Psdir\movies\CinemaList2.csv')))

movies = [m[0] for m in movies_list]

## I'm not entirely certain if all these movies are even still in the dataset but its too much work 
## figure out and this code doesn't hurt anything, right?
movies_wonky = {'Marvels The Avengers': 'the avengers',
                'The Kings Speech': 'king\'s speech',
                'Superman Man of Steel': 'man of steel',
                'X2 XMen United': 'x-men 2',
                'Transformers the Movie': 'Transformers',
                'XMen': 'x-men',
                '1214097 despicable me?': 'Despicable Me',
                '1083326 les miserables?': 'Les Miserables',
                'Brave 2012': 'Brave',
                'Pacific Rim 2013': 'Pacific Rim',
                'Doctor Strange 2016': 'Doctor Strange',
                'Wonder Woman 2017': 'Wonder Woman',
                'Star Wars Episode VI Return of the Jedi': 'Return of the Jedi',
                'Star Wars Episode VII The Force Awakens': 'The Force Awakens',
                'Men in Black III': 'Men in Black 3',
                'All the Presidents Men': 'All the President\'s Men',
                'Bugs Life': 'Bug\'s Life',
                'SpiderMan 2': 'Spider-man 2',
                'Mission Impossible 2': 'Mission Impossible II',
                'Mission Impossible 3': 'Mission Impossible III',
                'Oceans Eleven': 'Ocean\'s Eleven',
                'Oceans Twelve': 'Ocean\'s Twelve'
                }

boffice_gross = []
api_key = '822fae6f'
for m in movies:
    if m in movies_wonky.keys():
        json_url = 'http://www.omdbapi.com/?apikey=' + api_key + '&t=' + re.sub(' ', '+', movies_wonky[m])
    else:
        json_url = 'http://www.omdbapi.com/?apikey=' + api_key + '&t=' + re.sub(' ', '+', m)
    response = requests.get(json_url)
    response.raise_for_status()
    movie_data = json.loads(response.text)
    boffice_gross.append(movie_data['BoxOffice'])
    #print(m + "; " + movie_data['BoxOffice'] + ' : ' + str(len(boffice_gross))) # for debugging

for i, s in enumerate(boffice_gross): # Remove the Dollar signs and Commas to easier convert to ints
    boffice_gross[i] = re.sub('\$', '', re.sub('\,', '', s))
    
for t in movies_list: # append box office data to movies list
    t.append(boffice_gross[movies_list.index(t)])

for q in movies_list: # remove the NA's from my data set
    if q[4] == 'N/A':
        movies_list.remove(q) # Doesn't always remove all the N/A's Though

output = open('BofficeList.csv', 'w', newline = '') # save to a new CSV so I don't fuck up the old one
#output = open('BofficeList2.csv', 'w', newline = '')
out_writer = csv.writer(output)  
for r in movies_list:
    out_writer.writerow(r)
output.close()

