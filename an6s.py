from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.4,random_state=2)
print("training data",xtrain)
print("training data",ytrain)
print("testing data",xtest)
print("testing data",ytest)
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)
y_pred=gnb.predict(xtest)
from sklearn import metrics
print("accuracy is",metrics.accuracy_score(ytest,y_pred)*100)
