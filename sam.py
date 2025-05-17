import pandas as pd

file_url = ("C:/Users/kameswara.bharadwaj/OneDrive - Entain Group/Desktop/"
           "Quacca Regression observations.xlsx")
try:
    df = pd.read_excel(file_url,sheet_name='Quacca Regression observations',usecols=['Scenarios','Defect Id'])
    null_rows = df[df['Defect Id'].isna()]
    print(df.head())
    print(null_rows)
except FileNotFoundError:
    print("File not found at the specified location!")
except PermissionError:
    print("File is opened,unable to access!")