
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing csv datafile using pandas
train = pd.read_csv('glass.csv')

train.describe()

# to see all column names
print(train.keys())

# taking data as a dataframe
train1 = pd.DataFrame(train)

# taking feature data except(dropping) target column
X = train1.drop('Type', axis=1)
# taking target column
y = train1['Type']

# splitting data into train data for training model and test data for testing mode
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

# using Support Vector Machine model
from sklearn.svm import SVC
model = SVC()

# setting kernel to linear
param_grid = {'kernel': ['linear']}

#
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
plt.title('SVM linear Model')
plt.show()


# model.fit(X_train,y_train)
#
# predictions = model.predict(X_test)
#
# from sklearn.metrics import mean_squared_error
# print ('RMSE is: \n', mean_squared_error(y_test, predictions))
#
# acc_svc= round(model.score(X_train, y_train) * 100, 2)
# print("svmaccuracy is:", acc_svc)


