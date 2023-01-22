df = read.csv("C:/Users/User/OneDrive/Desktop/UN98.csv")

df = df[!is.na(df$GDPperCapita),]
df = within(df,rm(X,region))

m1 = lm(df$GDPperCapita~.,data = df)
summary(m1)

plot(m1)

library(car)
mmp(m1)
mmps(m1)
vif(m1)

selection = regsubsets(df$GDPperCapita~.,data = df, nvmax = NULL, method = "exhaustive")
plot(selection)

m2 = lm(df$GDPperCapita~df$educationFemale+df$lifeFemale+df$illiteracyFemale)
summary(m2)

vif(m2)

plot(m2)

shapiro.test(m2$residuals)

mmps(m2)

df3 = na.omit(df)
m3 = lm(df3$GDPperCapita~.,data = df3)
summary(m3)

summary(powerTransform(m3))
df3$GDPperCapita = log(df3$GDPperCapita)

m4 = lm(df3$GDPperCapita~.,data=df3)
summary(m4)
shapiro.test(m4$residuals)


selection2 = regsubsets(df3$GDPperCapita~.,data=df3,nvmax = NULL, method = "exhaustive")
plot(selection2)


m5 = lm(GDPperCapita~educationFemale+lifeFemale+illiteracyFemale,data=df3)
summary(m5)

par(mfrow=c(1,1))
plot(m5)

vif(m5)
shapiro.test(m5$residuals)
mmps(m5)

(exp(0.29399)-1)*100

anova(m1,m5)

plot(df$GDPperCapita,df$illiteracyFemale)
plot(df3$GDPperCapita,df3$illiteracyFemale)

mean(df3$GDPperCapita)

mean(df3$educationFemale)
mean(df3$lifeFemale)
mean(df3$illiteracyFemale)

log(mean(df$GDPperCapita))

predict(m5, newdata = data.frame(educationFemale = 10.75128, lifeFemale = 70.43333, illiteracyFemale = 22.57333),interval = "pred")
