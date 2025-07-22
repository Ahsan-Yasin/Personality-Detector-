import pandas as pd 
from data_ingestion import get_data  
from sklearn.model_selection import train_test_split 
import os 

def split(df : pd.DataFrame ): 
    train, test = train_test_split(df, test_size=0.1)  
    folder_path = 'data/train_test'                   
    os.makedirs(folder_path, exist_ok=True)

    train.to_csv(os.path.join(folder_path, "train.csv"), index=False)
    test.to_csv(os.path.join(folder_path, "test.csv"), index=False)

    return test,train
df=get_data('data/processed/processed_personality.csv') 
if __name__=='__main__':
    split(df)