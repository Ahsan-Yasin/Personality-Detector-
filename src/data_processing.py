#dataprocessing.py file  
import pandas as pd 
import numpy as np   
import os  
from data_ingestion import get_data
def process_personality_dataset(df: pd.DataFrame) -> pd.DataFrame: 
    df['Stage_fear']= df['Stage_fear'].map({"Yes":1,"No":0}) 
    df['Drained_after_socializing']=df['Drained_after_socializing'].map({"Yes":1,"No":0}) 
    df['Personality']=df['Personality'].map({"Extrovert":1,"Introvert":0}) 
    df=df.dropna()
    save_data(df)
    return df 

def save_data(df: pd.DataFrame) ->None:  
    try:
        folder_path = "data/processed"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "processed_personality.csv")
        df.to_csv(file_path, index=False)
    except Exception as e: 
        print("ERROR WHILE CREATING DATA FOLDER WITH PROCESSED CSV ")
        raise(e) 
  
df=get_data('raw_data/personality_dataset.csv')
process_personality_dataset(df) 