# "BusinessParking" ,"RestaurantsPriceRange2", "weekday_close_after_23", "weekend_close_after_23", "weekend_hour_g11", "tvslabel", "caterslabel", "delilabel",
# "outdoorlabel", "grouplabel", "wheellabel", "reservelabel", "noiselabel", "takeoutlabel",
# "cardlabel", "wifilabel", "bikelabel" 
# "RestaurantsPriceRange2", "noiselabel"
#             "weekday_close_after_23", "weekend_close_after_23", 
#             "weekend_hour_g11", "tvslabel", "caterslabel", "delilabel",
#             "outdoorlabel", "grouplabel", "wheellabel", "reservelabel", 
#              "takeoutlabel", "cardlabel", "wifilabel", 
#             "bikelabel" 





data=read.csv('merged.csv',sep=",")
m=lm(star~as.factor(bikelabel)+as.factor(wifilabel)+as.factor(cardlabel)+as.factor(takeoutlabel)
     + as.factor(noiselabel)+as.factor(reservelabel) +as.factor(wheellabel)+as.factor(grouplabel)
     +as.factor(outdoorlabel)+as.factor(delilabel)+as.factor(caterslabel)+as.factor(tvslabel) 
     +as.factor(weekend_hour_g11)+as.factor(weekend_close_after_23)+as.factor(weekday_close_after_23)
     +as.factor(city)+as.factor(BusinessParking)+as.factor(RestaurantsPriceRange2),data)
summary(m)
#noiselabel 1-noisy 2-average 3-quiet
#weekend_hour_g11 1-no 0-yes
#weekend_close_after_23 1-no 0-yes
#weekday_close_after_23 1-no 0-yes
#RestaurantsPriceRange2 1-common 2-expensive
#the rest: 1-yes 0-no

library(cvTools)
merged=read.csv('merged.csv',sep=",")
folds=cvFolds(nrow(merged),10,1)
rate_lm=rep(0,10)
i=1
train_index=folds$subsets[folds$which!=i,1]
validation_index=folds$subsets[folds$which==i,1]
n_train=length(train_index)
n_validation=length(validation_index)
train=merged[train_index,]
test=merged[validation_index,-1]
a=test[1,]
m=lm(star~as.factor(bikelabel)+as.factor(wifilabel)+as.factor(cardlabel)+as.factor(takeoutlabel)
     + as.factor(noiselabel)+as.factor(reservelabel) +as.factor(wheellabel)+as.factor(grouplabel)
     +as.factor(outdoorlabel)+as.factor(delilabel)+as.factor(caterslabel)+as.factor(tvslabel) +as.factor(weekend_hour_g11)+as.factor(weekend_close_after_23)+as.factor(weekday_close_after_23)+as.factor(city)+as.factor(BusinessParking)+as.factor(RestaurantsPriceRange2),data=train)
p=predict(m,test)