import pandas as pd

def convertToPandas(csv_name: str, separator: str = ',') -> pd.DataFrame:
    df = pd.read_csv(csv_name, sep = separator)
    df.replace(to_replace=' ', value=0, inplace=True)
    return df

