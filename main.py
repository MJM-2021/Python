import pandas as pd
import numpy as np
from datetime import date as dt

filename = 'bank_marketing.csv'
data = pd.read_csv(filename)

cl = ['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']
camp = ['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'last_contact_date']
econ = ['client_id', 'cons_price_idx', 'euribor_three_months']

data['job'] = data['job'].str.replace(".","_")

data['education'] = data['education'].str.replace(".","_")
data.loc[data['education'] == 'unknown' ,'education'] = np.nan

mapping = {'no':False, 'unknown':False, 'yes':True, 'nonexistent':False, 'failure':False, 'success':True}
data['credit_default'] = data['credit_default'].replace(mapping)
data['mortgage'] = data['mortgage'].replace(mapping)
data['campaign_outcome'] = data['campaign_outcome'].replace(mapping)
data['previous_outcome'] = data['previous_outcome'].replace(mapping)

data['year'] = '2022'
data['day'] = data['day'].astype('str')
data['last_contact_date'] = data['year'] + '-' + data['month'] + '-' + data['day']
data['last_contact_date'] = pd.to_datetime(data['last_contact_date'], infer_datetime_format=True, errors = 'coerce')

client = data[cl]
campaign = data[camp]
economics = data[econ]

client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)
