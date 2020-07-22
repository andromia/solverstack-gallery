import pandas as pd
import numpy as np
import os


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FLASK_STATIC_DIR = os.path.join(
    ROOT,
    'flask-app-gallery', 
    'app', 
    'static'
)
REACT_PUBLIC_DIR = os.path.join(
    ROOT,
    'react-app-gallery', 
    'public'
)

INPUT_DEMAND_FILENAME = 'vrp_testing_data.csv'
INPUT_ORIGINS_FILENAME = 'vrp_testing_origins.csv'

INPUT_DEMAND_FILEPATH = \
    os.path.join(ROOT, 'data', INPUT_DEMAND_FILENAME)
INPUT_ORIGINS_FILEPATH = \
    os.path.join(ROOT, INPUT_ORIGINS_FILENAME)

OUTPUT_DEMAND_FILENAME = 'vrp_demand.json'
OUTPUT_ORIGINS_FILENAME = 'vrp_origins.json'

FLASK_DEMAND_FILEPATH = \
    os.path.join(FLASK_STATIC_DIR, OUTPUT_DEMAND_FILENAME)
FLASK_ORIGINS_FILEPATH = \
    os.path.join(FLASK_STATIC_DIR, OUTPUT_ORIGINS_FILENAME)

REACT_DEMAND_FILEPATH = \
    os.path.join(FLASK_STATIC_DIR, OUTPUT_DEMAND_FILENAME)
REACT_ORIGINS_FILEPATH = \
    os.path.join(FLASK_STATIC_DIR, OUTPUT_ORIGINS_FILENAME)

def get_demand_df():
    df = pd.read_csv(os.path.join(ROOT, 'data', INPUT_DEMAND_FILENAME)
    df['cluster'] = np.random.randint(6, size=len(df))
    df['vehicle_id'] = np.random.randint(len(df), size=len(df))

    return df

def get_demand_json():
    df = get_demand_df()
    json = df.to_json(orient='records')

    return json

def create_demand_json():
    df = get_demand_df()

    # flask-app-gallery
    df.to_json(FLASK_DEMAND_FILEPATH, orient='records')

    # react-app-gallery
    df.to_json(REACT_DEMAND_FILEPATH, orient='records')

def get_origins_df():
    df = pd.read_csv(INPUT_ORIGINS_FILEPATH)

    return df

def get_origins_json():
    df = get_origins_df()
    json = df.to_json(orient='records')

    return json

def create_origins_json():
    df = get_origins_df()

    # flask-app-gallery
    df.to_json(FLASK_ORIGINS_FILEPATH, orient='records')

    # react-app-gallery
    df.to_json(REACT_ORIGINS_FILEPATH, orient='records')

if __name__ == '__main__':
    create_demand_json()
    create_origins_json()