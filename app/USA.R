data=read.csv("data/data.csv")
city_loc = matrix(c(-115.172813,36.114647,
                    -89.401230,43.073051,
                    -80.843124,35.227085,
                    -112.074036,33.448376,
                    -79.995888,40.440624,
                    -81.681290 , 41.505493),
                  byrow=T,ncol=2)
rownames(city_loc)=c("Las Vegas","Madison","Charlotte","Phoenix","Pittsburgh","Cleveland")
colnames(city_loc)=c("longtitude","latitude")

count=sort(table(data$city),decreasing=F)
city=names(count)
state_name=c('ohio','wisconsin','pennsylvania','north carolina','arizona','nevada') #ranked already
state=read.csv('data/state.csv')

# map_plot = function(){
color=colorRampPalette(c("yellow", "cyan"))(6)
# if(c=='None'){
m=matrix(c(1,2,2,2,2),ncol=5)
layout(m)
layout.show(2)
barplot(table(data$rate,data$city)[2:1,city],main="Number of Reviews",horiz=T,
        col=c("red","cyan"))
legend("bottomright",legend=c("4.0~5.0","0~4.0"),col=c("red","cyan"),pch=19,cex=1)
s_temp = state_name
s = state[,c('long','lat')]
map('state',col='lavenderblush',fill=TRUE)
map('state', s_temp, col=color, fill=TRUE,add=T)
legend("topleft",legend=paste(city,count),col=color,pch=15,ncol=2,cex=1)
title("Location Distribution")
# }else{
#   index=which(city==c)
#   s_temp = state_name[index]
#   s = state[state$region==s_temp,c('long','lat')]
#   par(mfrow=c(1,2))
#   map('state',xlim=range(s$long)+c(-1,1)*0.5,
#       ylim=range(s$lat)+c(-1,1)*0.5,
#       col='lavenderblush',fill=TRUE)
#   map('state', s_temp, col=color[index], fill=TRUE,add=T)
#   points(x=city_loc[c,1],y=city_loc[c,2],pch=19,col='blue')
#   legend('top',legend=c,col='blue',pch=19)
#   par(mfrow=c(1,1))
# }
#}