# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:13:43 2017

@author: Devlin
"""

from bs4 import BeautifulSoup
import requests
import re
import csv

# So im gonna try to find Rotten Tomatoes Scores for a bunch of movies the "easy way"

## Step 1: My List of Movies
movies_list = list(csv.reader(open('D:\Files\Psdir\movies\MList.csv')))

movies = [m[1] for m in movies_list]

del movies[0] # Remove the Title Row

for n in movies: # Remove Movies that don't have RT Ratings
    if n in ['Batman (1966)', 'Rush: Time Machine - Live in Cleveland (2011)']:
        movies.remove(n)
        
movies_wonky = {'Star Wars: A New Hope': 'Star Wars',
                'Star Wars: Return of the Jedi': 'Star Wars Episode VI Return of the Jedi',
                'Star Wars: Revenge of the Sith': 'Star Wars Episode III Revenge of the Sith',
                'Star Wars: The Empire Strikes Back': 'Empire Strikes Back',
                'Star Wars: The Force Awakens': 'Star Wars Episode VII The Force Awakens',
                'Man of Steel (2013)': 'Superman Man of Steel',
                'Ocean\'s Eleven (2001)': 'Oceans Eleven',
                'WALL•E': 'Wall E',
                'Avatar (Extended Collector\'s Edition)': 'Avatar',
                'Blade Runner (The Final Cut)': 'Blade Runner',
                'Spider-Man: Homecoming': 'Spider Man Homecoming',
                'The Amazing Spider-Man': 'The Amazing Spider Man',
                'The Hobbit: An Unexpected Journey (Extended Edition)': 'The Hobbit An Unexpected Journey',
                'The Hobbit: The Battle of the Five Armies (Extended Edition)': 'The Hobbit The Battle of the Five Armies',
                'The Hobbit: The Desolation of Smaug (Extended Edition)': 'The Hobbit The Desolation of Smaug',
                'The Lord of the Rings: The Fellowship of the Ring (Special Extended Edition)': 'The Lord of the Rings The Fellowship of the Ring',
                'The Lord of the Rings: The Return of the King (Special Extended Edition)': 'The Lord of the Rings The Return of the King',
                'The Lord of the Rings: The Two Towers (Extended Edition)': 'The Lord of the Rings The Two Towers',
                'X-Men: Apocalypse': 'X Men Apocalypse',
                'X-Men: Days of Future Past': 'X Men Days of Future Past',
                'X-Men: First Class': 'X Men First Class',
                'Mission: Impossible II': 'Mission: Impossible 2',
                'Mission: Impossible III': 'Mission: Impossible 3',
                'Anchorman: The Legend of Ron Burgundy': 'Anchorman',
                'The Avengers': 'Marvels The Avengers',
                'Wreck-It Ralph': 'Wreck it Ralph',
                'The Incredibles': 'Incredibles',
                'Transformers': 'Transformers the Movie',
                'A Fish Called Wanda': 'Fish Called Wanda',
                'Despicable Me': '1214097 despicable me?',
                'Les Miserables': '1083326 les miserables?',
                'Brave': 'Brave 2012',
                'Pacific Rim': 'Pacific Rim 2013',
                'A Bug\'s Life': 'Bugs Life',
                'The Bourne Identity': 'Bourne Identity',
                'Men In Black 3': 'Men in Black III'
                }
for k in movies_wonky.keys(): # Change names to match RT URLs
    if k in movies:
        movies[movies.index(k)] = movies_wonky[k]
        
        
blanks = [':', '(', ')', '!', ',', '\'', '-', '.'] 
for c in blanks: # Remobe all the special characters
    for i, m in enumerate(movies):
        movies[i] = m.replace(c, '')

               
#for x in sorted(movies):
#    print(x)
#print(len(movies)) # Check to Make Sure == 107

## Step 2: Rotten Tomatoes Scores
tomato_scores = []
for m in movies:
    RT_base_url = "https://www.rottentomatoes.com/m/"
    tomato_url = RT_base_url + re.sub(' ', '_', str(m))
    soup = BeautifulSoup(requests.get(tomato_url).text, "lxml")
    script = soup.findAll('script')[1].getText()
    indexes = script.find('ratingValue')
    tomato_scores.append([m, script[indexes + 13] + script[indexes + 14]])

for m in tomato_scores: # Clean up those weird "h's
    if m[1] == '"h':
        tomato_scores.remove(m)

output = open('TomatoList.csv', 'w', newline = '') # save to a new CSV so I don't fuck up the old one
out_writer = csv.writer(output)  
for r in tomato_scores:
    out_writer.writerow(r)
output.close()
    