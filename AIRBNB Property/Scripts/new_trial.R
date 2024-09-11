library(ggplot2)
library(GGally)
library(dplyr)

setwd("/Users/kunthshah/Desktop/archive/")
market_data <- read.csv("market2019FINAL.csv", header = TRUE, sep = ";")

# Converting data
market_data$guests <- as.numeric(market_data$guests)
market_data$month <- as.Date(paste(market_data$month, "-01", sep = ""), format = "%Y-%m-%d")
market_data$Hot.Tub <- as.logical(market_data$Hot.Tub)
market_data$Pool <- as.logical(market_data$Pool)

# Perform one-hot encoding for 'host_type'
market_data <- market_data %>%
  mutate(
    Professionals = as.integer(host_type == "Professionals"),
    `2-5 Units` = as.integer(host_type == "2-5 Units"),
    # `Single Owners` = as.integer(host_type == "Single Owners"),
  ) %>%
  select(-host_type) # Remove the original 'host_type' column

str(market_data)
summary(market_data)

# Filter data for only 'Professional' host_type
professional_data <- market_data %>%
  filter(Professionals == 1)

# Normalize predictor variables
predictor_vars <- professional_data[, c("bedrooms", "bathrooms", "guests", "openness", 
                                        "occupancy", "nightly.rate", "lead.time", 
                                        "length.stay", "Hot.Tub", "Pool")]
normalized_data <- scale(predictor_vars)
professional_data[, c("bedrooms", "bathrooms", "guests", "openness", 
                      "occupancy", "nightly.rate", "lead.time", 
                      "length.stay", "Hot.Tub", "Pool")] <- normalized_data

# Fit regression model with normalized predictor variables
regr_mod <- lm(revenue ~ bedrooms + bathrooms + guests + openness + occupancy + nightly.rate + lead.time + length.stay + Hot.Tub + Pool, data = professional_data)
summary(regr_mod)

plot(regr_mod)
