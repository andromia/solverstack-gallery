"""scripts run from /scripts"""
import pandas as pd
import numpy as np


def create_demand_json():
    df = pd.read_csv('../data/vrp_testing_data.csv')
    df['cluster'] = np.random.randint(6, size=len(df))
    df['vehicle_id'] = np.random.randint(len(df), size=len(df))

    # flask-app-gallery
    df.to_json('../flask-app-gallery/app/static/vrp_demand.json', orient='records')

    # react-app-gallery
    df.to_json('../react-app-gallery/public/vrp_demand.json', orient='records')

def create_origins_json():
    df = pd.read_csv('../data/vrp_testing_origins.csv')

    # flask-app-gallery
    df.to_json('../flask-app-gallery/app/static/vrp_origins.json', orient='records')

    # react-app-gallery
    df.to_json('../react-app-gallery/public/vrp_origins.json', orient='records')

if __name__ == '__main__':
    create_demand_json()
    create_origins_json()