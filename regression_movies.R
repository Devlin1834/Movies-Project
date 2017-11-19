setwd("D:/Files/Psdir/movies")

movies <- read.csv('BofficeList.csv', header = FALSE)
head(movies)

# So first I need to convert the cinema score grades to numbers. I might end up using
## dummy variables, but a numeric approach seems cleaner, if less interpretable

cinema_convert <- function(score) {
  letter <- factor(score, levels = c("A+", "A", "A-",
                                     "B+", "B", "B-",
                                     "C+", "C", "C-",
                                     "D+", "D", "D-",
                                     "F"))
  values <- c(seq(100, 0, by = -10))
  
  values[letter]
}

cinema_letters <- movies[4]
cinema_letters[] <- lapply(movies[4], cinema_convert)
movies[6] <- cinema_letters
colnames(movies) <- c("Movie", "TomatoScore", "MetaScore", "CinemaScore", "BoxOffice", "Cinema.Num")
write.csv(movies, 'RList.csv')

summary(movies)

## Thats all the data cleaning I need to do, now onto regressions
### T = TomatoMeter
### M = Metascore
### C = CinemaScore
### B = Boxoffice
### S  = Cinema.Num
### x seperates the Y and X's

## We start by trying to Predict the Box Office
BxT <- lm(BoxOffice ~ TomatoScore, data = movies)
summary(BxT)
plot(x = movies$TomatoScore, y = movies$BoxOffice)
abline(BxT)
# Terrible Model

BxM <- lm(BoxOffice ~ MetaScore, data = movies)
summary(BxM)
plot(x = movies$MetaScore, y = movies$BoxOffice)
abline(BxM)
# Another Terrible Model

BxS <- lm(BoxOffice ~ Cinema.Num, data = movies)
summary(BxS)
plot(x = movies$Cinema.Num, y = movies$BoxOffice)
abline(BxS)
# Best model so far and its still terrible

BxTMS <- lm(BoxOffice ~ TomatoScore + MetaScore + Cinema.Num, data = movies)
summary(BxTMS)
# Only slightly better than BxS\

# Heres Why all these models suck
hist(movies$BoxOffice) # Not Normal
hist(movies$TomatoScore) # Not Normal
hist(movies$MetaScore) # Fairly Normal
hist(movies$Cinema.Num) # Normal With Outlier

##Now lets try to predict Cinema Score
SxT <- lm(Cinema.Num ~ TomatoScore, data = movies)
summary(SxT)
plot(x = movies$TomatoScore, y = movies$Cinema.Num)
abline(SxT)
# Just God Awful

SxM <- lm(Cinema.Num ~ MetaScore, data = movies)
summary(SxM)
plot(x = movies$MetaScore, y = movies$Cinema.Num)
abline(SxM)
# Still Pretty Bad

## Lets Try to Predict MetaCritic with Rotten Tomatos
MxT <- lm(MetaScore ~ TomatoScore, data = movies)
summary(MxT)
plot(x = movies$TomatoScore, y = movies$MetaScore)
abline(MxT)
# Well duh its a good model, but at least its something


