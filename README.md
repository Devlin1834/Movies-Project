# Movies-Project
Comparing Metacritic and Rotten Tomatoes to see who can better predict CinemaScores and Box Office Gross


(1) movies.R - pulls a list of movies from my iTunes Library

    --> MList.csv (109 Data Points)
  
(2) movies.py - uses BeuatifulSoup to parse rotten tomatoes and prints each movies tomatoscores to a new csv

    --> TomatoList.csv (104 Data Points)
  
(3) meta _ movies.py - uses an Open Movies Database API to pull metacritic scores for each movie and save them to a csv

    --> MeatList.csv (92 Data Points)
  
(4) cinema _ movies.py - uses pyautogui to save each movies cinema score as an image to be added to a csv manually

    --> CimenaList1.csv (53 Data Points) - Contains only movies for which the script correctly pulled the score
  
    --> CinemaList2.csv (84 Data Points) - Contains movies in CinemaList1 with the gaps filled in by hand
    
    --> Cinema Folder Contains the image results of the script
  
(5) boffice _ movies.py - uses the Open Movies Database API to get the boxoffice numbers for each remaining movies
        
        --> BofficeList.csv (49 Data Points) - uses CinemaList1.csv as base
        
        --> BofficeList2.csv (76 Data Points) - uses CinemaList2.csv as base
        
(6) regression _ movies.R - Cleans and tries to find relationships between the data. Spoilers: There are none

        --> RList.csv (49 Data Points)
        
        --> Reg Vis folder contains the charts returned from the script

__Plans__

(7) Try to find some cool visualizations anyways

(8) Repeat steps 6 & 7 with CinemaList2 to see if the extra data helps at all
