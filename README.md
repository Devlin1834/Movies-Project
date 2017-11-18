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
  
__Plans__

(5) Pull Box Office Data for each film

(6) Send back to R for statistical Analysis and Visualization
