from DataConversion.convert import convertToPandas
# importing the modules
import pandas as pd


class Backend:
    def __init__(self):
        self.__dataPand = convertToPandas('DataConversion\\trimmed_data.csv')
        self.__drugs = list()

    def addMedication(self, drug: str):
        self.__drugs.append(drug)

    def __checkInteractions(self) -> pd.DataFrame:
        # get all interactions between drugs in self.__drugs
        # iterate over list and only check the one coming after the current one
        return self.__dataPand.loc[(self.__dataPand['object'].isin(self.__drugs)) & (self.__dataPand['precipitant'].isin(self.__drugs))]

    def getWarnings(self) -> pd.DataFrame:
        interactions = self.__checkInteractions()
        return interactions.loc[(pd.to_numeric(interactions['severity']) == 1) | (pd.to_numeric(interactions['severity']) == 2)]

    def getErrors(self) -> pd.DataFrame:
        interactions = self.__checkInteractions()
        return interactions.loc[pd.to_numeric(interactions['severity']) == 3]