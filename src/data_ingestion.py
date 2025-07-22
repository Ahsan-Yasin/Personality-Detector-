#data ingestion file 
import numpy as np 
import pandas as pd  

#this function will fetch data 
def get_data(file_name): 
    try: 
        df=pd.read_csv(file_name)
        return df 
    except Exception as e:
        print('ERROR WHILE READING FILE ')
        raise(e) 
