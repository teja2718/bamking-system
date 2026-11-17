import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,roc_curve,auc,ConfusionMatrixDisplay
data=load_breast_cancer()
X=data.data
y=data.target
X_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(x_tarin)
X_test=scaler.transform(X_test)
from skleran.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
cm=confusion_matrix(y_test,y_pred)
print("Confusion Matrix:\n",cm)
ConfusionMatrixDisplay(cm,display_labels=data.target_names).plot()
plt.title("Confusion Matrix")
plt.show()
print("Classification Report:\n",classification_reportly(y_test,y_pred,target_names=data.target_names))
y_proba=model.predict_proba(X_test)[:,1]
n