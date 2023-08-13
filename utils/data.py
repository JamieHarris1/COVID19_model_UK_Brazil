import typing
import pandas as pd

class Data:
    def load_data(file_name: str) -> pd.DataFrame:
        column_names = ['Date', 'Cases', 'Fatalities']
        data = pd.read_csv(file_name, names = column_names)
        data['Date'] = pd.to_datetime(data['Date'])
        data['Fatalities'] = data['Fatalities'].astype(int)
        data['Cases'] = data['Cases'].astype(int)
        data['Day'] = range(0, len(data))
        return data