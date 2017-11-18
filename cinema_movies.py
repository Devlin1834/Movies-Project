# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:21:12 2017

@author: Devlin
"""

import pyautogui as pag
import time
import re
import csv
'''
So the goal was to grab a screenshot of each movies cinemascore then
try to train a machine learning algorithim to interpret the pictures
and save them to a csv for me.
two problems:
    1. cinemascores search bar is a joke. Even whe you search for 
    a movies exact title, another movie can stil be the number one
    result. and its all some wird picture thing so theres no
    html to parse and get the right one. 
        SO if you only save a picture of the letter grade theres
        no garuntee you got the right movie. You need the name too
    2. This follows from number one, a lot of what i managed to save 
    the wrong movie. Meaning I have to go back and look over what I
    have by hand anyways
So you might be asking, whats the point of the script then doofus?
well it simplifies what I'm looking at and puts it all in one folder
so I just need to browse the folder to find the score and not do a lot
of tedius searching on the website
'''
## Step 1: Get a list of movies top work with

# File generated with R based on my iTunes Library
# We need to use this one because it still has the special characters in 
# the movie titles
movies_list = list(csv.reader(open('D:\Files\Psdir\movies\MList.csv')))

movies = [m[1] for m in movies_list] # Remove the row numbers
        
movies_wonky = {'Star Wars: A New Hope': 'Star Wars',
                'Star Wars: Return of the Jedi': 'Return of the Jedi',
                'Star Wars: Revenge of the Sith': 'Revenge of the Sith',
                'Star Wars: The Empire Strikes Back': 'Empire Strikes Back',
                'Star Wars: The Force Awakens': 'The Force Awakens',
                'WALL•E': 'Wall E',
                'Avatar (Extended Collector\'s Edition)': 'Avatar',
                'Blade Runner (The Final Cut)': 'Blade Runner',
                'Spider-Man: Homecoming': 'Homecoming',
                'The Amazing Spider-Man': 'Amazing Spider-Man',
                'The Hobbit: An Unexpected Journey (Extended Edition)': 'An Unexpected Journey',
                'The Hobbit: The Battle of the Five Armies (Extended Edition)': 'The Battle of the Five Armies',
                'The Hobbit: The Desolation of Smaug (Extended Edition)': 'The Desolation of Smaug',
                'The Lord of the Rings: The Fellowship of the Ring (Special Extended Edition)': 'The Fellowship of the Ring',
                'The Lord of the Rings: The Return of the King (Special Extended Edition)': 'The Return of the King',
                'The Lord of the Rings: The Two Towers (Extended Edition)': 'The Two Towers',
                'A Fish Called Wanda': 'Fish Called Wanda',
                'The Bourne Identity': 'Bourne Identity',
                'A Bug\'s Life': 'Bug\'s Life',
                'Marvels The Avengers': 'the avengers',
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
                'Men in Black III': 'Men in Black 3',
                'All the Presidents Men': 'All the President\'s Men',
                'SpiderMan 2': 'Spider-man 2',
                'Mission Impossible 2': 'Mission Impossible II',
                'Mission Impossible 3': 'Mission Impossible III',
                'Oceans Eleven': 'Ocean\'s Eleven',
                'Oceans Twelve': 'Ocean\'s Twelve'
                }
for k in movies_wonky.keys(): # Change names to better match titles
    if k in movies:
        movies[movies.index(k)] = movies_wonky[k]

for i, m in enumerate(movies): # Becuase Cinemascore puts the 'the'
    if m[0:3] == 'The':        # at the end, need to remove from front
        movies[i] = m.replace('The ', '')

## Step 2: Save a picture of each movies CinemaScore

chrome = (564, 1062) # Open Chrome
address = (221, 47) # Click the Address Bar
search = (811, 396) # Click on Cinemascores Search Bar
start = (21, 1062) # Open the start menu
paint = (455, 540) # Open Paint
crop_start = (1003, 667) # Where to start the Crop
crop_end = (1471, 717) # Where to end the Crop
save_bar = (1143, 329) # The save windoes address bar
file_name = (908, 721) # the filename bar

url = 'https://www.cinemascore.com/'
save_dir = 'D:\Files\Psdir\movies\cinema'

for i, name in enumerate(movies):
    pag.click(chrome, duration = 0.25)         #
    pag.click(address, duration = 0.25)        # All of this is highly
    pag.typewrite(url)                         # situational. The locations
    pag.typewrite(['enter'])                   # of things change as you
    pag.click(search, duration = 5)            # use them, so if running
    pag.typewrite(name)                        # this script again
    time.sleep(2.5)                            # it would probably be best
    pag.typewrite(['printscreen'])             # to double check that
    pag.click(start)                           # all the pointer locations
    pag.click(paint, duration = 0.25)          # still click the right
    time.sleep(1)                              # spot. 
    pag.hotkey('ctrl', 'v')                    #
    time.sleep(0.25)                           
    pag.hotkey('ctrl', 'shift', 'x')           
    pag.click(crop_start, duration = 1)        
    pag.dragTo(crop_end, duration = 0.25)      
    pag.hotkey('ctrl', 'x')                    
    pag.hotkey('ctrl', 'n')
    time.sleep(0.25)
    pag.typewrite(['right', 'enter'])
    pag.hotkey('ctrl', 'v')
    time.sleep(0.25)
    pag.hotkey('ctrl', 's')
    pag.click(save_bar)
    time.sleep(0.5)
    pag.typewrite(save_dir)
    time.sleep(0.5)
    pag.typewrite(['enter'])
    pag.click(file_name)
    time.sleep(0.5)
    pag.typewrite(str(i) + "__" + re.sub('\:', '', re.sub('\.', '', re.sub(' ', '_', name))))
    time.sleep(.5)
    pag.typewrite(['enter'])
    time.sleep(0.5)
    pag.hotkey('alt', 'f4')
    time.sleep(0.5)
    pag.hotkey('alt', 'f4')
    time.sleep(0.5)


# This Script gives 53 correct matches necessary out of 84 - .63