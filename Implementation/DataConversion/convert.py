import pandas as pd

def convertToPandas(csv_name: str, separator: str = ',') -> pd.DataFrame:
    df = pd.read_csv(csv_name, sep = separator)
    df.replace(to_replace=' ', value=0, inplace=True)
    return df

def convertToDict(csv_name: str, separator: str = ',') -> dict:

    df = pd.read_csv(csv_name, sep=separator)

    df = df.reset_index()  # make sure indexes pair with number of rows

    keys = df['object'].unique()
    data = dict()

    for key in keys:
        data[key] = dict()

    for index, row in df.iterrows():
        try:
            _, _, objectId = row['drug1'].split(':')
        except AttributeError:
            objectId = row['drug1']
        except ValueError:
            objectId = row['drug1']

        try:
            _, _, interactionId = row['drug2'].split(':')
        except AttributeError:
            interactionId = row['drug2']
        except ValueError:
            interactionId = row['drug1']

        data[row['object']]['Id'] = objectId

        data[row['object']][row['precipitant']] = dict()
        data[row['object']][row['precipitant']]['Id'] = interactionId
        data[row['object']][row['precipitant']]['severity'] = row['severity']

    return data

