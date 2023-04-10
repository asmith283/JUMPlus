import pandas as pd
from forex_python.converter import CurrencyRates

def dataCleaner(df):
    df = df.dropna(how='all').drop('sofifa_id', axis=1) #drops complete rows that contain all null #i am also not doing normalization for the table
    df = df.drop(columns=['goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes']) #removing duplicated columns
    df = df.rename(columns={'wage_eur': "wage_usd", "value_eur": "value_usd", "release_clause_eur" : "release_clause_usd"}) #changes title eur to usd
    df[["wage_usd", "value_usd", "release_clause_usd"]] = df[["wage_usd", "value_usd", "release_clause_usd"]].apply(lambda x: CurrencyRates().convert('EUR', 'USD', x)) #converts EUR to USD
    #changes all float columns besides currency to int
    df[['team_jersey_number', 'contract_valid_until','nation_jersey_number', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning' ]] = df[['team_jersey_number', 'contract_valid_until','nation_jersey_number', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning' ]].astype('Int64')
    df['body_type'] =  df['body_type'].replace(['Akinfenwa', 'C. Ronaldo', 'Courtois', 'Messi', 'Neymar', 'PLAYER_BODY_TYPE_25', 'Shaqiri'], 'Unique') #all incorrect body types changed to unique
    return df