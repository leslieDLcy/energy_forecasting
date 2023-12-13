import pandas as pd
from darts import TimeSeries
from darts.dataprocessing.transformers import MissingValuesFiller

def get_series_by_zone(df, identifier, id):
    
    """ concat into one series by zone 
    
    args:
        identifier: 'id' or 'station_id'
        id: int; 
    """
    df_zone1 = df[df[identifier] == int(id)]
    df_zone1 = df_zone1.drop(columns=[identifier])
    series_list_z1 = create_series_list(df_zone1)
    concated = pd.concat(series_list_z1)
    return concated


# create a list of series

def create_series_list(df):
    
    """ transform row append into column """
    
    series_list = []
    for i in range(len(df)):
        st_stamp = df.iloc[i].name
        index = pd.date_range(st_stamp, periods=24, freq='H')
        series = pd.Series(data=df.iloc[i].values, index=index, dtype='float32')
        series_list.append(series)
    return series_list



def change_timeindex(df):
    """ change the timeindex in df """
    df['Datetime'] = pd.to_datetime(df[['year', 'month', 'day']])
    df = df.set_index('Datetime')
    df = df.drop(columns = ['year', 'month', 'day'])
    return df



def fill_missing(incomplete_series):
    """ propcessing to fill in missing values """
    
    filler = MissingValuesFiller()
    filled = filler.transform(TimeSeries.from_series(incomplete_series))

    return filled
