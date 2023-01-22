dfp <- read.csv("C:/Users/User/OneDrive/Documents/Code/R/working directory/PSID1976.csv")

dfp$participation[dfp$participation=="no"]<-0
dfp$participation[dfp$participation=="yes"]<-1
dfp$city[dfp$city=="no"]<-0
dfp$city[dfp$city=="yes"]<-1
dfp$college[dfp$college=="no"]<-0
dfp$college[dfp$college=="yes"]<-1
dfp$hcollege[dfp$hcollege=="no"]<-0
dfp$hcollege[dfp$hcollege=="yes"]<-1

dfp<-transform(dfp, participation = as.integer(participation),city = as.integer(city), college= as.integer(college), hcollege=as.integer(hcollege))

dfp = dfp[-c(1,3,8,9)]

m1p = glm(participation~.,data = dfp, family = binomial)
summary(m1p)
vif(m1p)

range(dfp$youngkids)
dfp$youngkids[dfp$youngkids==0]=10^-5
range(dfp$oldkids)
dfp$oldkids[dfp$oldkids==0]=10^-5
range(dfp$age)
range(dfp$education)
range(dfp$hhours)
range(dfp$hage)
range(dfp$heducation)
range(dfp$hwage)
range(dfp$fincome)
range(dfp$tax)
range(dfp$meducation)
dfp$meducation[dfp$meducation==0]=10^-5
range(dfp$feducation)
dfp$feducation[dfp$feducation==0]=10^-5
range(dfp$unemp)
range(dfp$experience)
dfp$experience[dfp$experience==0]=10^-5


trans = powerTransform(cbind(dfp$youngkids,dfp$oldkids,dfp$age,dfp$education,dfp$hhours,dfp$hage,dfp$heducation,dfp$hwage,dfp$fincome,dfp$tax,dfp$meducation,dfp$feducation,dfp$unemp,dfp$experience))
summary(trans)

dfp2 = data.frame(dfp$participation,dfp$youngkids^-0.42,dfp$oldkids^0.16,dfp$age^0.5,dfp$education,dfp$hhours^0.7,dfp$hage,dfp$heducation^1.38,dfp$hwage^0.33,dfp$fincome^0.33,dfp$tax^1.73,dfp$meducation^0.77,dfp$feducation^0.69,dfp$unemp^0.68,dfp$city,dfp$experience^0.43,dfp$college,dfp$hcollege)
m2p = glm(dfp2$dfp.participation~.,data=dfp2, family = binomial)
summary(m2p)

mmps(m1p)

mmps(m2p)

dfp3 = data.frame(dfp$participation,dfp$youngkids,dfp$oldkids,dfp$age,dfp$education,dfp$hhours^0.7,dfp$hage,dfp$heducation^1.38,dfp$hwage,dfp$fincome,dfp$tax,dfp$meducation,dfp$feducation,dfp$unemp,dfp$city,dfp$experience^0.43,dfp$college,dfp$hcollege)
m3p = glm(dfp3$dfp.participation~.,data=dfp3, family = binomial)
summary(m3p)

mmps(m3p)

library(leaps)
exh = regsubsets(dfp3$dfp.participation ~ ., data = dfp3, nvmax = NULL, method = "exhaustive")
summary(exh)$bic
plot(exh)

m4p = glm(dfp3$dfp.participation~dfp3$dfp.youngkids+dfp3$dfp.age+dfp3$dfp.education+dfp3$dfp.hhours.0.7+dfp3$dfp.hwage+dfp3$dfp.tax+dfp3$dfp.experience.0.43, family = binomial)
summary(m4p)

mmps(m4p)
vif(m4p)

mmp(m4p)

logodds = m4p$linear.predictors
boxTidwell(logodds~dfp3$dfp.youngkids+dfp3$dfp.age+dfp3$dfp.education+dfp3$dfp.hhours.0.7+dfp3$dfp.hwage+dfp3$dfp.tax+dfp3$dfp.experience.0.43)

par(mfrow=c(2,2))
plot(logodds~dfp3$dfp.experience.0.43)
plot(logodds~dfp3$dfp.age)
plot(logodds~dfp3$dfp.education)
plot(logodds~dfp3$dfp.tax)

logodds2 = m2$linear.predictors
par(mfrow=c(2,2))
plot(logodds2~df$experience)
plot(logodds2~df$age)
plot(logodds2~df$education)
plot(logodds2~df$tax)

trans2 = powerTransform(cbind(dfp3$dfp.hwage,dfp3$dfp.tax))
summary(trans2)

dfp5=data.frame(dfp3$dfp.participation,dfp3$dfp.youngkids,dfp3$dfp.age,dfp3$dfp.education,dfp3$dfp.hhours.0.7,dfp3$dfp.hwage^0.33,dfp3$dfp.tax^2,dfp3$dfp.experience.0.43)
m5p = glm(dfp5$dfp3.dfp.participation~.,data=dfp5,family = binomial)
summary(m5p)
mmps(m5p)


x=c(1,mean(dfp3$dfp.youngkids),mean(dfp3$dfp.age),mean(dfp3$dfp.education),mean(dfp3$dfp.hhours.0.7),mean(dfp3$dfp.hwage),mean(dfp3$dfp.tax),mean(dfp3$dfp.experience.0.43))
logodds = sum(coef(m4p)*x)
prob = exp(sum(coef(m4p)*x))/(1+exp(sum(coef(m4p)*x)))

mean(dfp$participation)
logodds
prob

confint(m4p)

anova(m1p,m4p, test="Chisq")


m2 <- glm(df$participation~oldkids+education+hhours+youngkids+age+hwage+tax+experience, family="binomial",data=df)
summary(m2)

confint(m2)

anova(m2,m1, test="Chisq")



backwardBIC=step(m1, direction = "backward", k=log(n))
