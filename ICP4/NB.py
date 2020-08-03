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

# splitting data into train data for training model and test data for testing model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

# using naive bayes model
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

# fitting model to our train data
gnb.fit(X_train,y_train)

# testing the model comparing with test data
predictions = gnb.predict(X_test)

# print(predictions)

# calculating root mean sqaure value of the errors
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

# calculating accuracy
from sklearn import metrics
print("Accuracy:",round(metrics.accuracy_score(y_test, predictions) * 100, 2))
print("classification_report\n",metrics.classification_report(y_test,predictions))
print("confusion matrix\n",metrics.confusion_matrix(y_test,predictions))

# plotting the actual values (test data) with the predicted vales made by our model
actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Value')
plt.ylabel('Actual Actual Value')
plt.title('Naive Bayes Model')
plt.show()

