import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.datasets import  load_boston
from sklearn.metrics import  mean_squared_error


df= pd.read_csv('USA_Housing.csv')


# FEAUTURES
X=df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

#PREDICTION
Y=df['Price']

#Splitting the training data and test data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.4,random_state=101)

lm = LinearRegression()
lm.fit(X_train,Y_train)
Y_pred=lm.predict(X_test);


cdf=pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])

##
boston = load_boston()



plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
##plt.show()

##

customers=pd.read_csv("Ecommerce_Customers.csv")
X=customers[[ 'Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']]
Y=customers['Yearly Amount Spent']
X_train,x_test,Y_train,y_test= train_test_split(X,Y,test_size=0.3,random_state=101)
lm.fit(X_train,Y_train)
cdf=pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])

Y_predictions=lm.predict(x_test)

plt.scatter(y_test, Y_predictions)
plt.xlabel("$Y_test")
plt.ylabel("Predicted Y: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()

