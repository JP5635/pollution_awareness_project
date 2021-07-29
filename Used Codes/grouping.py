# creating tables for each disease must substitute indexing to get specific data wanted

import pandas as pd
import argparse

eastm07_11d = pd.read_csv('c_east_metro 07-11.CSV',encoding = 'ISO-8859-1')
eastm12_16d = pd.read_csv('c_east_metro 12-16.CSV',encoding = 'ISO-8859-1')
gellong07_11d = pd.read_csv('c_geelong 07-11.CSV',encoding = 'ISO-8859-1')
gellong12_16d = pd.read_csv('c_geelong 12-16.CSV',encoding = 'ISO-8859-1')
gippsland07_11d = pd.read_csv('c_gippsland 07-11.CSV',encoding = 'ISO-8859-1')
gippsland12_16d = pd.read_csv('c_gippsland 12-16.CSV',encoding = 'ISO-8859-1')
nwm07_11d = pd.read_csv('c_nw_metro 07-11.CSV',encoding = 'ISO-8859-1')
nwm12_16d = pd.read_csv('c_nw_metro 12-16.CSV',encoding = 'ISO-8859-1')
southm07_11d = pd.read_csv('c_south_metro 07-11.CSV',encoding = 'ISO-8859-1')
southm12_16d = pd.read_csv('c_south_metro 12-16.CSV',encoding = 'ISO-8859-1')

eastm07_11d = eastm07_11d['Standardised Rate per 100,000 Persons']
eastm12_16d = eastm12_16d['Standardised Rate per 100,000 Persons']
gellong07_11d = gellong07_11d['Standardised Rate per 100,000 Persons']
gellong12_16d = gellong12_16d['Standardised Rate per 100,000 Persons']
gippsland07_11d = gippsland07_11d['Standardised Rate per 100,000 Persons']
gippsland12_16d = gippsland12_16d['Standardised Rate per 100,000 Persons']
nwm07_11d = nwm07_11d['Standardised Rate per 100,000 Persons']
nwm12_16d = nwm12_16d['Standardised Rate per 100,000 Persons']
southm07_11d = southm07_11d['Standardised Rate per 100,000 Persons']
southm12_16d = southm12_16d['Standardised Rate per 100,000 Persons']


eastm07_11n = pd.read_csv('east_metro(normalize) 07-11.csv',encoding = 'ISO-8859-1')
eastm12_16n = pd.read_csv('east_metro(normalize) 12-16.csv',encoding = 'ISO-8859-1')
gellong07_11n = pd.read_csv('geelong(normalize) 07-11.csv',encoding = 'ISO-8859-1')
gellong12_16n = pd.read_csv('geelong(normalize) 12-16.csv',encoding = 'ISO-8859-1')
gippsland07_11n = pd.read_csv('gippsland(normalize) 07-11.csv',encoding = 'ISO-8859-1')
gippsland12_16n = pd.read_csv('gippsland(normalize) 12-16.csv',encoding = 'ISO-8859-1')
nwm07_11n = pd.read_csv('nw_metro(normalize) 07-11.csv',encoding = 'ISO-8859-1')
nwm12_16n = pd.read_csv('nw_metro(normalize) 12-16.csv',encoding = 'ISO-8859-1')
southm07_11n = pd.read_csv('south_metro(normalize) 07-11.csv',encoding = 'ISO-8859-1')
southm12_16n = pd.read_csv('south_metro(normalize) 12-16.csv',encoding = 'ISO-8859-1')

eastm07_11n.insert(2, 'Region', ['East_Metro']*len(eastm07_11n), True)
eastm07_11n.insert(1, 'Death_Rate', [eastm07_11d[1]]*len(eastm07_11n), True)
eastm12_16n.insert(2, 'Region', ['East_Metro']*len(eastm12_16n), True)
eastm12_16n.insert(1, 'Death_Rate', [eastm12_16d[9]]*len(eastm12_16n), True)

gellong07_11n.insert(2, 'Region', ['Geelong']*len(gellong07_11n), True)
gellong07_11n.insert(1, 'Death_Rate', [gellong07_11d[9]]*len(gellong07_11n), True)
gellong12_16n.insert(2, 'Region', ['Geelong']*len(gellong12_16n), True)
gellong12_16n.insert(1, 'Death_Rate', [gellong12_16d[9]]*len(gellong12_16n), True)

gippsland07_11n.insert(2, 'Region', ['Gippsland']*len(gippsland07_11n), True)
gippsland07_11n.insert(1, 'Death_Rate', [gippsland07_11d[9]]*len(gippsland07_11n), True)
gippsland12_16n.insert(2, 'Region', ['Gippsland']*len(gippsland12_16n), True)
gippsland12_16n.insert(1, 'Death_Rate', [gippsland12_16d[9]]*len(gippsland12_16n), True)

nwm07_11n.insert(2, 'Region', ['NorthE_Metro']*len(nwm07_11n), True)
nwm07_11n.insert(1, 'Death_Rate', [nwm07_11d[9]]*len(nwm07_11n), True)
nwm12_16n.insert(2, 'Region', ['NorthE_Metro']*len(nwm12_16n), True)
nwm12_16n.insert(1, 'Death_Rate', [nwm12_16d[9]]*len(nwm12_16n), True)

southm07_11n.insert(2, 'Region', ['South_Metro']*len(southm07_11n), True)
southm07_11n.insert(1, 'Death_Rate', [southm07_11d[9]]*len(southm07_11n), True)
southm12_16n.insert(2, 'Region', ['South_Metro']*len(southm12_16n), True)
southm12_16n.insert(1, 'Death_Rate', [southm12_16d[9]]*len(southm12_16n), True)

final07_11 = pd.concat([eastm07_11n, gellong07_11n, gippsland07_11n, nwm07_11n, southm07_11n]).reset_index(drop = True)
final12_16 = pd.concat([eastm12_16n, gellong12_16n, gippsland12_16n, nwm12_16n, southm12_16n]).reset_index(drop = True)
final07_11.to_csv('Skin-Cancer07-11.csv',index=False)
final12_16.to_csv('Skin-Cancer12-16.csv',index=False)


