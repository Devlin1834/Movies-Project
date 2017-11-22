setwd("D:/Files/Psdir/movies")

library(ggplot2)
library(reshape2)

movies_theme <- theme(
  plot.title = element_text(face = 'bold.italic', size = '18', color = 'black'),
  axis.title = element_text(face = 'bold', size = '12', color = 'black'),
  axis.text = element_text(face = 'italic', size = '10', color = 'black'),
  axis.ticks = element_blank(),
  panel.background = element_rect(fill = 'white', color = 'white'),
  panel.grid.major.x = element_line(linetype = 2, color = 'black'),
  panel.grid.major.y = element_line(linetype = 2, color = 'black'),
  panel.grid.minor.x = element_blank(),
  panel.grid.minor.y = element_blank(),
  panel.border = element_rect(fill = NA, color = 'black')
)

# I'm going to use RList2 for the extra data #
movies <- read.csv('RList2.csv')

plus <- c(100, 70, 40)
none <- c(90, 60, 30)
minus <- c(80, 50, 20)

A <- c(100, 90, 80)
B <- c(70, 60, 50)
C <- c(40, 30, 20)

movies$Letter <- seq(1:76)
movies$Grade <- seq(1:76)

for (row in 1:nrow(movies)){
  num <- movies[row, 'Cinema.Num']
  if (num %in% plus) {
    movies[row, 'Grade'] <- '+'
  }
  if (num %in% none){
    movies[row, 'Grade'] <- '~'
  }
  if (num %in% minus){
    movies[row, 'Grade'] <- '-'
  }
  if (num %in% A) {
    movies[row, 'Letter'] <- 'A'
  }
  if (num %in% B){
    movies[row, 'Letter'] <- 'B'
  }
  if (num %in% C){
    movies[row, 'Letter'] <- 'C'
  }
}
movies$Cinema.Num <- sapply(movies$Cinema.Num, as.character)
ggplot(movies, aes(x = TomatoScore, y = MetaScore, color = Letter, size = Grade)) + 
  geom_point() + geom_point(pch = 21, color = 'black') +
  movies_theme + 
  labs(title = 'Scores Summary', x = 'Tomato Score', y = 'MetaScore') + 
  scale_size_manual(values = c(2, 4, 6)) + 
  scale_color_manual(values = c('gold', 'dodgerblue', 'red')) + 
  scale_x_continuous(breaks = c(0,20,40,60,80,100), limits = c(0,100)) + 
  scale_y_continuous(breaks = c(0,20,40,60,80,100), limits = c(0,100))

lbs = c('A-', 'A', 'A+', 'B-', 'B', 'B+', 'C-', 'C', 'C+')
colors = c('gold', 'gold', 'gold', 'dodgerblue', 'dodgerblue', 'dodgerblue', 'red', 'red', 'red')
sizes = c(2, 4, 6, 2, 4, 6, 2, 4, 6)

ggplot(movies, aes(x = TomatoScore, y = MetaScore, color = Cinema.Num, size = Cinema.Num)) + 
  geom_point() + geom_point(pch = 21, color = 'black') + 
  movies_theme + 
  labs(title = 'Scores Summary', x = 'Tomato Score', y = 'MetaScore') + 
  scale_size_manual(values = sizes, name = 'CinemaScore', labels = lbs) + 
  scale_color_manual(values = colors, name = 'CinemaScore', labels = lbs) + 
  scale_x_continuous(breaks = c(0,20,40,60,80,100), limits = c(0,100)) + 
  scale_y_continuous(breaks = c(0,20,40,60,80,100), limits = c(0,100))

ggplot(movies, aes(x = CinemaScore, fill = Letter)) + 
  geom_histogram(stat = 'count') + movies_theme + 
  scale_fill_manual(values = c('gold', 'dodgerblue', 'red')) + 
  labs(title = 'CinemaScore Distibution', y = '')

ggplot(movies, aes(x = MetaScore, fill = Letter)) + 
  geom_histogram(binwidth = 5, alpha = 0.75) + movies_theme + 
  scale_fill_manual(values = c('gold', 'dodgerblue', 'red')) + 
  scale_y_continuous(breaks = seq(0:13), limits = c(0,13)) + 
  scale_x_continuous(breaks = c(0,10,20,30,40,50,60,70,80,90,100), limits = c(0,100)) + 
  labs(title = 'Distribution of MetaScores', y = '') + geom_hline(yintercept = 0)

ggplot(movies, aes(x = TomatoScore, fill = Letter)) + 
  geom_histogram(binwidth = 5, alpha = 0.75) + movies_theme + 
  scale_fill_manual(values = c('gold', 'dodgerblue', 'red')) + 
  scale_y_continuous(breaks = seq(0:13), limits = c(0,13)) + 
  scale_x_continuous(breaks = c(0,10,20,30,40,50,60,70,80,90,100), limits = c(0,100)) + 
  labs(title = 'Distribution of Tomato Scores', y = '') + geom_hline(yintercept = 0)

breaks = seq(0,1000000000, by = 125000000)
labels = c('$0', '', '$250,000,000', '', '$500,000,000', '', '$750,000,000', '', '$1,000,000,000')

ggplot(movies, aes(x = BoxOffice, fill = Letter)) + geom_histogram(binwidth = 50000000, alpha = 0.75) + 
  scale_fill_manual(values = c('gold', 'dodgerblue', 'red')) + movies_theme + 
  scale_y_continuous(breaks = seq(1:21)) + labs(title = "Box Office Gross Distribution", y = '') + 
  scale_x_continuous(labels = labels, breaks = breaks)+ geom_hline(yintercept = 0)

ggplot(movies, aes(y = TomatoScore, x = '')) + geom_violin(fill = 'darkblue') + movies_theme + 
  labs(x = 'Tomato Score', y = '', title = 'TomatoScore Violin')
ggplot(movies, aes(y = MetaScore, x = '')) + geom_violin(fill = 'gold4') + movies_theme + 
  labs(x = 'MetaScore', y = '', title = 'MetaScore Violin')
ggplot(movies, aes(y = BoxOffice, x = '')) + geom_violin(fill = 'firebrick4') + movies_theme + 
  labs(x = 'BoxOffice', y = '', title = 'BoxOffice Violin') + 
  scale_y_continuous(breaks = breaks, labels = labels)

