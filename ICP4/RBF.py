import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


train = pd.read_csv('glass.csv')

train.describe()

print(train.keys())

train1 = pd.DataFrame(train)

X = train1.drop('Type', axis=1)
y = train1['Type']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

from sklearn.svm import SVC
model = SVC()

# model.fit(X_train,y_train)

# predictions = model.predict(X_test)

# param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']}

param_grid = {'kernel': ['rbf']}
from sklearn.model_selection import GridSearchCV
grid = GridSearchCV(SVC(),param_grid,refit=True)
grid.fit(X_train,y_train)
grid_predictions = grid.predict(X_test)

from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, grid_predictions))

acc_svc= round(grid.score(X_train, y_train) * 100, 2)
print("svmaccuracy is:", acc_svc)

actual_values = y_test
plt.scatter(grid_predictions, actual_values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Value')
plt.ylabel('Actual Actual Value')
plt.title('SVM rbf Model')
plt.show()
