library(jsonlite)
setwd("~/Dropbox/Work/00. Active Projects/315. Data Share (very large)")
#library(rjson)
#testfile <- fromJSON(file="Electronics.json")
jsonfile <- "Electronics.json"
dat <- fromJSON(sprintf("[%s]", paste(readLines(jsonfile), collapse=",")))
dim(dat)
str(dat)

ratings <- dat$'review/score'
ratings <- sort(ratings)
hist(ratings)

val <- 1352068320
theDateTime <- as.POSIXct(val, origin="1970-01-01")
theDate <- as.Date(as.POSIXct(val, origin="1970-01-01"))

timer <-  as.POSIXct(dat$'review/time', origin="1970-01-01")
dat2 <- dat

test4<-aggregate(cbind(dat2$'review/score', dat2$'review/helpful')~dat2$'review/time', data=dat2, sum, na.rm=TRUE)

newdata <- dat2[c(-13, -14, -15)]

reviewer<-aggregate(cbind(newdata$'review/score', newdata$'review/helpful')~newdata$'review/profileName', data=newdata, mean, na.rm=TRUE)

plot(reviewer$V2~reviewer$V1, xlab="Mean Reviewer Review", ylab="Mean Helpfulness Ratings")

countofreviews<-aggregate(cbind(newdata$'review/score', newdata$'review/helpful')~newdata$'review/profileName', data=newdata, count, na.rm=TRUE)
