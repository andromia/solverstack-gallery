# solverstack-open-gallery

Open-sourced data visualizations.

## vrp_demand.json

Actual vrp input data with randomized output data for visualizing.

```python
import pandas as pd
import numpy as np

df = pd.read_csv('data/vrp_testing_data.csv')
df['cluster'] = np.random.randint(6, size=len(df))
df['vehicle_id'] = np.random.randint(len(df), size=len(df))
df.to_json('<app-gallery>/<path>/<to>/<public/static>/vrp_data.json', orient='records')
```
