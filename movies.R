setwd("D:/Files/Psdir/movies")

library(XML)

ituneslib <- readKeyValueDB("iTunes Music Library.xml")
tracksxml <- ituneslib$Tracks
tracks <- lapply(tracksxml, data.frame)
songs <- ldply(tracks)

movies <- songs[which(songs$Movie==TRUE),]
movies <- movies[3]
movies <- unique(movies)
rownames(movies) <- NULL
write.csv(movies, "MList.csv")
