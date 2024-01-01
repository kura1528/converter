import os
import pandas as pd
import glob

file_name = glob.glob("client-excel/*.xlsx")[0]
json_file_name = "output.json"

# Reading and converting excel to json using pandas
excel_data = pd.read_excel(file_name)
json_data = excel_data.to_json(orient='records')

# JSON Output
print('JSON Output')
print(excel_data)

# Creating JSON file
with open(json_file_name, 'w') as json_file:
	json_file.write(json_data)

# Done
print('Excel is converted into JSON')
