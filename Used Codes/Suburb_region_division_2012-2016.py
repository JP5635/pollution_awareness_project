import pandas as pd
import math

def normalize(dataset):
    x = 0
    for num in dataset:
        x += num**2
    norm = math.sqrt(x)
    for i in range(len(dataset)):
        dataset[i] = round(dataset[i]/norm, 3)
    return dataset

csv_name = '2012-16_overall_average.csv'
csv = pd.read_csv(csv_name)

csv.set_index('sp_name',inplace=True)


east_metro = round(csv.loc['Box.Hill'].groupby(['param_id']).mean().reset_index(), 2)
south_metro = round(csv.loc['Brighton'].groupby(['param_id']).mean().reset_index(), 2)
nw_metro = round(csv.loc[['Richmond', 'Footscray', 'Alphington', 'Melton', 'Point Cook', 'Altona North', 'Dandenong', 'Mooroolbark']].groupby(['param_id']).mean().reset_index(), 2)
geelong = round(csv.loc['Geelong South'].groupby(['param_id']).mean().reset_index(), 2)
gippsland = round(csv.loc[['Traralgon','Morwell South','Morwell East', 'Churchill']].groupby(['param_id']).mean().reset_index(), 2)

east_metro['value'] = normalize(east_metro['value'].tolist())
south_metro['value'] = normalize(south_metro['value'].tolist())
nw_metro['value'] = normalize(nw_metro['value'].tolist())
geelong['value'] = normalize(geelong['value'].tolist())
gippsland['value'] = normalize(gippsland['value'].tolist())

east_metro.to_csv('east_metro(normalize) 12-16.csv', index = False)
south_metro.to_csv('south_metro(normalize) 12-16.csv', index = False)
nw_metro.to_csv('nw_metro(normalize) 12-16.csv', index = False)
geelong.to_csv('geelong(normalize) 12-16.csv', index = False)
gippsland.to_csv('gippsland(normalize) 12-16.csv', index = False)