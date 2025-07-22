import numpy as np 
import pandas as pd  


def get_data(name): 
    try: 
        df=pd.read_csv('name')
        return df 
    except Exception as e:
        print('ERROR WHILE READING FILE ')
        raise(e)
df=get_data('personality_dataset.csv') 
df.head()