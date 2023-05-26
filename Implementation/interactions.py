from builtins import object

from DataConversion.convert import convertToPandas
import numpy as np
from backend import MedicationData
# importing the modules
import pandas as pd


class Interactions:
    def __init__(self):
        self.__dataPand = convertToPandas('DataConversion\\trimmed_data.csv')

    def __checkInteractions(self, drugs: pd.DataFrame) -> pd.DataFrame:
        objects = [drug.strip() in list(drugs['Medication']) for drug in list(self.__dataPand['object'])]
        precipitants = [drug.strip() in list(drugs['Medication']) for drug in list(self.__dataPand['precipitant'])]
        return self.__dataPand.loc[np.array(objects) & np.array(precipitants)]

    def getWarnings(self, drugs: pd.DataFrame) -> pd.DataFrame:
        interactions = self.__checkInteractions(drugs)
        ret = interactions.loc[(pd.to_numeric(interactions['severity']) == 1) | (pd.to_numeric(interactions['severity']) == 2)]
        del ret["drug1"]
        del ret["drug2"]
        return ret

    def getErrors(self, drugs: pd.DataFrame) -> pd.DataFrame:
        interactions = self.__checkInteractions(drugs)
        ret = interactions.loc[pd.to_numeric(interactions['severity']) == 3]
        del ret["drug1"]
        del ret["drug2"]
        return ret

