import pandas as pd 
from sklearn.linear_model import LogisticRegression
from data_ingestion import get_data  
from sklearn.metrics import classification_report, accuracy_score
import joblib 
import os

def split(df):
    x = df.iloc[:, :-1]  
    y = df.iloc[:, -1]    
    return x, y

def make_model(df):  
    x, y = split(df)  

    model = LogisticRegression()
    model.fit(x, y)

    folder_path = "models"
    os.makedirs(folder_path, exist_ok=True)
    model_path = os.path.join(folder_path, "personality_model.pkl")
    joblib.dump(model, model_path)
    return model 

def model_eval(model, train, test):
    x_test, y_test = split(test) 
    x_train, y_train = split(train)   

    y_pred = model.predict(x_test)  
    
    report = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    path = 'models/report'
    os.makedirs(path, exist_ok=True)
    report_path = os.path.join(path, "personality_model_report.txt")

    with open(report_path, "w") as f:
        f.write("Classification Report:\n")
        f.write(report + "\n")
        f.write(f"Accuracy: {accuracy}")


train = get_data('data/train_test/train.csv')
test = get_data('data/train_test/test.csv') 
model = make_model(train) 
model_eval(model, train, test)  
