library(glmtoolbox)
library(ggplot2)
library(pROC)

# Load the dataset
setwd("/Users/kunthshah/Desktop/Financial Dataset/")
data <- read.csv("data_modified.csv", header = TRUE, sep = ",")

# Convert binary values column to factor
data$y <- factor(data$y, levels = c("No", "Yes"))
data$default <- factor(data$default, levels = c("no", "yes"))
data$housing <- factor(data$housing, levels = c("no", "yes"))
data$loan <- factor(data$loan, levels = c("no", "yes"))

# plotting boxplot graphs before addressing outliers
boxplot(balance ~ y, data, main = "Balance Boxplot")
boxplot(duration ~ y, data, main = "Duration Boxplot")
boxplot(day ~ y, data, main = "Day Boxplot")
boxplot(age ~ y, data, main = "Age Boxplot")


# Function to remove outliers
remove_outliers <- function(data, var_name) {
  outliers <- boxplot.stats(data[[var_name]])$out
  data <- data[!(data[[var_name]] %in% outliers), ]
  return(data)
}

# Remove outliers for balance variable
data <- remove_outliers(data, "balance")

# Remove outliers for duration variable
data <- remove_outliers(data, "duration")

# Remove outliers for day variable
data <- remove_outliers(data, "day")

# Remove outliers for age variable
data <- remove_outliers(data, "age")

# Replot boxplot graphs after addressing outliers
boxplot(balance ~ y, data, main = "Balance Boxplot")
boxplot(duration ~ y, data, main = "Duration Boxplot")
boxplot(day ~ y, data, main = "Day Boxplot")
boxplot(age ~ y, data, main = "Age Boxplot")



# Exploring y against numeric values
m1= glm(y~ data$balance, data = data, family = binomial)
summary(m1)
m2= glm(y~ data$duration, data = data, family = binomial)
summary(m2)
m3= glm(y~ data$day, data = data, family = binomial)
summary(m3)
m4= glm(y~ data$age, data = data, family = binomial)
summary(m4)

# Exploring y against other Binary[yes]
m5= glm(y~ default, data = data, family = binomial)
summary(m5)
m6= glm(y~ housing, data = data, family = binomial)
summary(m6)
m7= glm(y~ loan, data = data, family = binomial)
summary(m7)

#M Testing Logistic Regression
M0= glm(y~ balance + duration + day + age, data = data, family = binomial)
summary(M0)
hltest(M0) #test the validity of model


#M Finalized Logistic Regression
MX= glm(y~ balance + duration + day + age, data = data, family = binomial)
summary(MX)
hltest(MX) #test the validity of model

probs=predict(MX,type = "response")
summary(probs)

# Calculate contrasts for 'y' (0 for "No", 1 for "Yes")
contrasts(data$y)
modX_pred <- rep("No", 10000)
modX_preds <- predict(MX, type = "response")
modX_pred[modX_preds > 0.5] <- "Yes"
modX_pred
table(modX_pred, data$y)

# Calculate the error rate, removing NA values
mean(modX_preds != data$y)

# Create ROC curve object
R = roc(data$y, modX_preds)
best_threshold <- coords(R, "best", ret = "threshold")
modX_pred[modX_preds > best_threshold] <- "Yes"
table(modX_pred, data$y)

# Calculate error rate
error_rate <- mean(modX_pred != data$y, na.rm = TRUE)
error_rate

# Plot ROC curve
plot(R)

AUC <- auc(R)

# Print percentage of area covered
cat("Area Under the ROC Curve:", round(AUC * 100, 2), "%\n")


