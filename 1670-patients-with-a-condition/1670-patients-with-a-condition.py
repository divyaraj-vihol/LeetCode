import pandas as pd
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    def has_type1_diabetes(conditions):
        return any(code.startswith('DIAB1') for code in conditions.split())
    filtered_patients = patients[patients['conditions'].apply(has_type1_diabetes)]
    return filtered_patients[['patient_id', 'patient_name', 'conditions']]
