import pandas as pd


class MedicationData:
    medication_df = pd.DataFrame

    def add_new_medication(self, medication_name, manufacturer):
        new_med = {'Medication': medication_name, 'Manufacturer': manufacturer}
        new_medication_row_df = pd.DataFrame([new_med])
        pd.concat([self.medication_df, new_medication_row_df], ignore_index=True)
        return self.medication_df

    def set_medication_data(self, df):
        self.medication_df = df

    def get_mediction_data(self):
        return self.medication_df

    def import_file(self, filepath):
        med_csv_data = pd.read_csv(filepath)
        self.medication_df = med_csv_data
        return med_csv_data

    def export_file(self, filepath):
        self.medication_df.to_csv('saved_medication.csv', index=False)
