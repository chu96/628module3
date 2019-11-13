library(OptimalCutpoints)
ice=read.csv('~/Desktop/1909/628/module3/ice1.csv',sep=",")
ice$star_cate=ifelse(ice$stars<4,0,1)
head(ice)
optimal.cutpoint.Youden<-optimal.cutpoints(X = "weekday_open", status = "star_cate", tag.healthy = 1, methods = "Youden", data = ice, pop.prev = NULL,  control = control.cutpoints(), ci.fit = TRUE, conf.level = 0.95, trace = FALSE)
optimal.cutpoint.Youden
optimal.cutpoint.Youden<-optimal.cutpoints(X = "weekday_close", status = "star_cate", tag.healthy = 1, methods = "Youden", data = ice, pop.prev = NULL,  control = control.cutpoints(), ci.fit = TRUE, conf.level = 0.95, trace = FALSE)
optimal.cutpoint.Youden
optimal.cutpoint.Youden<-optimal.cutpoints(X = "weekend_open", status = "star_cate", tag.healthy = 1, methods = "Youden", data = ice, pop.prev = NULL,  control = control.cutpoints(), ci.fit = TRUE, conf.level = 0.95, trace = FALSE)
optimal.cutpoint.Youden
optimal.cutpoint.Youden<-optimal.cutpoints(X = "weekend_close", status = "star_cate", tag.healthy = 1, methods = "Youden", data = ice, pop.prev = NULL,  control = control.cutpoints(), ci.fit = TRUE, conf.level = 0.95, trace = FALSE)
optimal.cutpoint.Youden
optimal.cutpoint.Youden<-optimal.cutpoints(X = "businesstime", status = "star_cate", tag.healthy = 1, methods = "Youden", data = ice, pop.prev = NULL,  control = control.cutpoints(), ci.fit = TRUE, conf.level = 0.95, trace = FALSE)
optimal.cutpoint.Youden

##cut point for weekday and weekend open time  is not significant,
## cut point for close time is 23:00,
## cut point for weekend business time is 11 hours.


star=read.csv('~/Desktop/1909/628/module3/compute_star.csv',sep=",")
business=read.csv('~/Desktop/1909/628/module3/ice_final3.csv',sep=",")
merged=merge(star,business )
merged$caterslabel[1]=0
m=lm(star~as.factor(bikelabel)+as.factor(wifilabel)+as.factor(cardlabel)+as.factor(takeoutlabel)
+ as.factor(noiselabel)+as.factor(reservelabel) +as.factor(wheellabel)+as.factor(grouplabel)
+as.factor(outdoorlabel)+as.factor(delilabel)+as.factor(kidlabel)+as.factor(tvslabel) +as.factor(weekend_hour_g11)+as.factor(weekend_close_after_23)+as.factor(weekday_close_after_23)+as.factor(city)+as.factor(caterslabel),data=merged)
