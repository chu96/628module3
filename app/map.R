### map
# library(maps)     # Draw geographical maps.
# library(mapdata)  # Map databases.

# state = map_data('state')
# data = read.csv('D:/3. 2019 Fall/STAT 628/module 3/Part II/merged.csv',sep=",")
# 
# state_name = c('nevada','arizona','wisconsin','north carolina','pennsylvania','ohio')
# city_name = as.character(unique(data$city))
# f = function(city){
#   return(state_name[which(city_name==city)])
# }
# data$state = sapply(data$city,f)
# state=state[state$region %in% state_name,]
# write.csv(state,'state.csv')

# map('state')
# map('state', state_name, col='gray90', fill=TRUE,add=T)
# with(state, points(long, lat, pch=16, col='black', cex=.25))
# loc=state[,c('long','lat','region')]
# # for(i in 1:length(city_name)){
# #   loc_temp=colMeans(loc[which(loc$region==state_name[i]),-3])
# #   text(loc_temp,labels=city_name[i])
# # }
# box()
# map.scale(ratio=FALSE, metric=FALSE)


library(leaflet)
library(maps)
# library(htmlwidgets)
setwd('D:/3. 2019 Fall/STAT 628/module 3/app/')
state=read.csv('state.csv')
state_name = c('nevada','arizona','wisconsin','north carolina','pennsylvania','ohio')
bounds <- map('state',state_name, fill=TRUE)
# A custom icon.
icons <- awesomeIcons(
  icon = 'disc',
  iconColor = 'black',
  library = 'ion', # Options are 'glyphicon', 'fa', 'ion'.
  markerColor = 'blue',
  squareMarker = TRUE
)
# Create the Leaflet map widget and add some map layers.
# We use the pipe operator %>% to streamline the adding of
# layers to the leaflet object. The pipe operator comes from 
# the magrittr package via the dplyr package.
map <- leaflet(data = state) %>% 
  addProviderTiles("Esri.WorldShadedRelief", group = "Relief") %>%
  addPolygons(data=bounds, group="States", weight=2, fillOpacity = 0) %>%
  addScaleBar(position = "bottomleft") %>%
  addLayersControl(
    baseGroups = "Relief",
    overlayGroups = "States",
    options = layersControlOptions(collapsed = FALSE)
  )
invisible(print(map))
