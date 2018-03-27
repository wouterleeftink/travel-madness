library(ggplot2)
library(ggmap)

data1 <- read.csv('accidents_2005_to_2007.csv')
data2 <- read.csv('accidents_2009_to_2011.csv')
data3 <- read.csv('accidents_2012_to_2014.csv')

comb_data <- rbind(data1, data2)
accidents <- rbind(comb_data, data3)

completeFun <- function(data, desiredCols) {
  completeVec <- complete.cases(data[, desiredCols])
  return(data[completeVec, ])
}

accidents <- completeFun(accidents, c('Longitude', 'Latitude'))
mean(accidents$Longitude)
mean(accidents$Latitude)
mapgilbert <- get_map(location = c(lon = -4, lat = 54.00366), zoom = 6,
                      maptype = "satellite", scale = 2)

latlons <- accidents[c('Longitude', 'Latitude')]
lon <- as.vector(accidents$Longitude)
lat <- as.vector(accidents$Latitude)
ggmap(mapgilbert) + geom_density2d(data = latlons, 
        aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = latlons, 
        aes(x = lon, y = lat, fill = ..level.., alpha = ..level..), size = 0.01, 
        bins = 2000, geom = "polygon") + scale_fill_gradient(low = "green", high = "red", 
        guide = FALSE) + scale_alpha(range = c(0, 0.3), guide = FALSE)