import numpy as nm 
import matplotlib.pyplot as mtp 
import pandas as pd 
data_set= pd.read_csv('user_data.csv') 
data_set 
x= data_set.iloc[:, [2,3]].values 
y= data_set.iloc[:, 4].values 
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0) 
from sklearn.preprocessing import StandardScaler 
st_x= StandardScaler() 
x_train= st_x.fit_transform(x_train) 
x_test= st_x.transform(x_test) 
from sklearn.linear_model import LogisticRegression 
classifier= LogisticRegression(random_state=0) 
classifier.fit(x_train, y_train) 
y_pred = classifier.predict(x_test) 

#Predicting the training set result 

y_pred_train = classifier.predict(x_train) 
acc_score=accuracy_score(y_test,y_pred) 
print('Accuracy Score:',acc_score) 
print('*'*65)
from sklearn.metrics import confusion_matrix 
cm= confusion_matrix(y_test,y_pred) 
print('Confusion Matrix\n',cm) 
print('*'*65) 
clf_report=classification_report(y_test,y_pred) 
print('CR',clf_report) 


print("**************************************************")


#Training Data Evaluation 
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve 

acc_score=accuracy_score(y_train,y_pred_train) 

print('Accuracy Score:',acc_score) 
print('*'*65) 
from sklearn.metrics import confusion_matrix 
cm= confusion_matrix(y_train,y_pred_train) 
print('Confusion Matrix\n',cm) 
print('*'*65) 
clf_report=classification_report(y_train,y_pred_train) 
# print('CR’, clf_report) 
