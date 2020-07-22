#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TODO: use scripts.create_vrp_data
# sys.path.append('../') failing
import pandas as pd
import numpy as np
from json import loads

import os

ROOT = os.path.dirname(os.path.abspath(''))

def check_data(data, name:str):
    """
    Print len of data.
    
    :data:       pandas dataframe or list-like
    :name:       str of name for data
    
    returns null
    """
    print(f'{name}: {len(data)}')

origins = pd.read_csv(os.path.join(ROOT, 'data', 'vrp_testing_origins.csv'))
origins = loads(origins.to_json(orient='records'))
check_data(origins, 'origins')

demand = pd.read_csv(os.path.join(ROOT, 'data', 'vrp_testing_data.csv'))
demand['cluster'] = np.random.randint(6, size=len(demand))
demand['vehicle_id'] = np.random.randint(len(demand), size=len(demand))
demand = loads(demand.to_json(orient='records'))
check_data(demand, 'demand')

