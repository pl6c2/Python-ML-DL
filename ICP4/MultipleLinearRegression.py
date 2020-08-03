import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wine = pd.read_csv('winequality-red.csv')
# wine.dropna()
print(wine.isnull().sum())

df = pd.DataFrame(wine)
print('top 3 correlated columns are :\n' + str(df[df.columns[:]].corr()['quality'][:11].sort_values(ascending=True)[5:8]))


# X = wine[['alcohol', 'sulphates','citric acid']]
X = wine.drop('quality',axis=1)
y = wine['quality']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.2)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)


# coeff = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])


predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
# plt.show()


# R-squared is a statistical measure of how close the data are to the fitted regression line
from sklearn.metrics import r2_score

print('r2 score is ',r2_score(y_test,predictions))

from sklearn.metrics import mean_squared_error
print('rmse',mean_squared_error(y_test,predictions))
