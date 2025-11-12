import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error ,r2_score 
import matplotlib.pyplot as plt 

def MarvellousHeadBrainLinear(Datapath):

    Line = "*"*50

    df = pd.read_csv(Datapath)
    print(Line)
    print("First Few records of the dataseta are :- ")
    print(Line)
    print(df.head())
    print(Line)


    print("Statistical information of dataset:-")
    print(Line)
    print(df.describe())
    print(Line) 


    X = df[['Head Size(cm^3)']]
    Y = df[['Brain Weight(grams)']]

    print("Independant varibales are :- Head Size")
    print("Dependant varibales are :- Brain Weight")

    print("Total Records in datasets:-",X.shape)

    X_train ,X_test ,Y_train , Y_test = train_test_split(X,Y,test_size=0.2 , random_state =42)

    print("Dimensions of training datasets:",X_train.shape)
    print("Dimension of testing datasets :-",X_test.shape)


    model = LinearRegression()
    model.fit(X_train,Y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(Y_test,y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y_test,y_pred)

    


    print("Visual representaion :-")

    plt.figure(figsize = (8,5))
    plt.scatter(X_test,Y_test,color = 'blue',label ='Actual')
    plt.plot(X_test.values.flatten(),y_pred , color ='Red',linewidth=2,label='Regresiion Line')
    plt.xlabel('Head Size (cm^3)')
    plt.ylabel('Brain Weight(grams)')

    plt.title("MarvellousHeadBrainRegression")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Result of Case Study :-")
    print("Slop of line (m):-",model.coef_[0])
    print("Intercept (c):-",model.intercept_)
    print("Mean suare error is :-",mse)
    print(" Root Mean suare error is :-",rmse)
    print("R sqaure value :-",r2)





def main():

    MarvellousHeadBrainLinear("MarvellousHeadBrain.csv")

if __name__ =="__main__":
    main()