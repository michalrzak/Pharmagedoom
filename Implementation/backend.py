import pandas as pd

class MedicationData:
    columns_ = ['Medication', 'Manufacturer']
    medication_df = None

    def __init__(self):
        self.medication_df = pd.DataFrame(columns=self.columns_)

    def add_new_medication(self, medication_name: str, manufacturer: str):
        new_med = {'Medication': medication_name, 'Manufacturer': manufacturer}
        self.medication_df.loc[len(self.medication_df.index)] = new_med

    def set_medication_data(self, df):
        self.medication_df = df

    def get_medication_data(self):
        return self.medication_df

    def get_medication_name(self):
        return self.medication_df['Medication']

    def import_file(self, filepath):
        med_csv_data = pd.read_csv(filepath)
        self.medication_df = med_csv_data
        return med_csv_data

    def export_file(self, filepath):
        self.medication_df.to_csv(filepath, index=False)
