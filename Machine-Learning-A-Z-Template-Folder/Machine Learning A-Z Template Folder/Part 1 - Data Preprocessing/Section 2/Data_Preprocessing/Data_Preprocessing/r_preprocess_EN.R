


# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# missing dataset
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x,na.rm = TRUE)),
                     dataset$Salary)