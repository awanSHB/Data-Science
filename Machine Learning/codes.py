
# 1) For Predicting From model

'''
print('---------[700,900]---------')
wg = 700
vol = 900
co2 = regressor.predict([[wg,vol]])
print(co2)
print('--------[1100,1500]----------')
wg = 1100
vol = 1500
co2 = regressor.predict([[wg,vol]])
print(co2)
print('--------[1500,2500]----------')
wg = 1500
vol = 2500
co2 = regressor.predict([[wg,vol]])
print(co2)
'''

# 1) For checking observations are independent or not

'''
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson
import matplotlib.pyplot as plt

# Load your dataset into a pandas DataFrame
data = pd.read_csv('your_dataset.csv')

# Separate the features (independent variables) and the target variable (dependent variable)
X = data.drop('target_variable', axis=1)
y = data['target_variable']

# Add a constant column to the features
X = sm.add_constant(X)

# Fit the logistic regression model
logit_model = sm.Logit(y, X)
result = logit_model.fit()

# Get the residuals
residuals = result.resid

# Plot residuals vs. order of observations
plt.scatter(range(len(residuals)), residuals, marker='o', color='blue')
plt.xlabel('Order of Observations')
plt.ylabel('Residuals')
plt.title('Residuals vs. Order of Observations')
plt.show()

# Perform Durbin-Watson test for autocorrelation
durbin_watson_statistic = durbin_watson(residuals)
print(f"Durbin-Watson Statistic: {durbin_watson_statistic}")
'''


## 2) eigen values for multicollinearity

'''
import pandas as pd
import numpy as np

# Load your dataset into a pandas DataFrame
data = pd.read_csv('your_dataset.csv')

# Separate the features (independent variables)
X = data.drop('target_variable', axis=1)

# Calculate the covariance matrix
cov_matrix = X.cov()

# Calculate the eigenvalues
eigenvalues = np.linalg.eigvals(cov_matrix)

# Calculate the condition number
condition_number = np.max(eigenvalues) / np.min(eigenvalues)

# Display the eigenvalues and condition number
print("Eigenvalues:")
print(eigenvalues)
print("Condition Number:", condition_number)
'''

## 3) Variable inflation factor

'''
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load your dataset into a pandas DataFrame
data = pd.read_csv('your_dataset.csv')

# Separate the features (independent variables)
X = data.drop('target_variable', axis=1)

# Add a constant column to the features
X = sm.add_constant(X)

# Calculate VIF for each independent variable
vif = pd.DataFrame()
vif["Variable"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# Display the VIF values
print(vif)
'''


## 4) Select Features using lasso regression
'''
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso

X, y = make_regression(n_samples=1000, n_features=30, random_state=42)
lasso = Lasso(alpha=0.1)  # alpha is the regularization parameter

lasso.fit(X, y)

feature_importances = lasso.coef_
selected_features = feature_importances != 0
X_selected = X[:, selected_features]

-----------
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, random_state=42)

'''

## 5) Dummies
'''
dummies = pd.get_dummies(X.Gender)

X = pd.concat([X, dummies], axis = 'columns')
'''

## 6) Cross Validation

'''
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load or create your dataset
# For example, assuming you have a DataFrame named df containing features and target variable
# X = df[['Age', 'EstimatedSalary']]
# y = df['Purchased']

# Split the dataset into training and testing sets (optional, if you already have separate train and test sets)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Naive Bayes classifier (GaussianNB in this case)
gnb = GaussianNB()

# Perform cross-validation with 5 folds
# Here, we use accuracy as the scoring metric, but you can use other metrics such as 'precision', 'recall', 'f1', etc.
# Cross-validation returns an array of scores for each fold
# The mean and standard deviation of these scores can be used to assess the model's performance
scores = cross_val_score(gnb, X_train, y_train, cv=5, scoring='accuracy')

# Print the cross-validation scores
print("Cross-validation scores:", scores)
print("Mean cross-validation score:", np.mean(scores))
print("Standard deviation of cross-validation scores:", np.std(scores))

'''