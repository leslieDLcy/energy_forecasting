import pandas as pd
import numpy as np



def date_formatting(df):
    """ recipe for datetime indexing of dataframe """
    
    return (df
            .assign(datetime = pd.to_datetime(df['Date'], format='%Y%m%d%H'))  
            .set_index('datetime', drop=True)
           )


def remove_tailnan(df):
    """ Remove nan values from the excess in the dataframe """

    df = df.drop(index=pd.date_range(start='2008-06-30 06:00:00', end=df.index[-1], freq='H'))
    return df


def check_missing(df):
    """ quickly see how many missing values are left in the dataframe """
    
    print("No of missing values left:", np.sum(df.isna()))
