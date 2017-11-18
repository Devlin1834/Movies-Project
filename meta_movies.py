# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:20:57 2017

@author: Devlin
"""

import json
import re
import requests
import csv

movies_list = list(csv.reader(open('D:\Files\Psdir\movies\TomatoList.csv')))

movies = [m[0] for m in movies_list]

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

#for m in movies:
#    print(m)
#print(len(movies)) # Should == 103
    
## Metacritic Scores
meta_scores = []
skipped = []
api_key = '822fae6f'
for m in movies:
    if m in movies_wonky.keys():
        json_url = 'http://www.omdbapi.com/?apikey=' + api_key + '&t=' + re.sub(' ', '+', movies_wonky[m])
    else:
        json_url = 'http://www.omdbapi.com/?apikey=' + api_key + '&t=' + re.sub(' ', '+', m)
    response = requests.get(json_url)
    response.raise_for_status()
    movie_data = json.loads(response.text)
    try:
        meta_scores.append(movie_data['Ratings'][2]['Value'])
    except IndexError:
        skipped.append(m)
        continue
    #print(m + "; " + movie_data['Ratings'][2]['Value'] + ' : ' + str(len(meta_scores)))

for p in movies_list:  # For some reason this doesn't remove Mission Impossible 2
    if p[0] in skipped:
        movies_list.remove(p)
        
del movies_list[86] # Remove Mission Impossible 2
            
for p in movies_list: # Add the Metacritic Score to DataFrame
    p.append(meta_scores[movies_list.index(p)][0:2])

output = open('MetaList.csv', 'w', newline = '') # save to a new CSV so I don't fuck up the old one
out_writer = csv.writer(output)  
for r in movies_list:
    out_writer.writerow(r)
output.close()

    
        