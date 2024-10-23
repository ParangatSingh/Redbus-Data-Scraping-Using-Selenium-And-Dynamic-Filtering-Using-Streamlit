import pandas as pd
import os

file_path = (os.path.join(os.getcwd()))

ap = pd.read_csv(file_path + '/merge_10_state/andhra_bus_data.csv')

chand = pd.read_csv(file_path + '/merge_10_state/chandigarh_bus_data.csv')

himachal = pd.read_csv(file_path + '/merge_10_state/himachal_bus_data.csv')

kerala = pd.read_csv(file_path + '/merge_10_state/kerala_bus_data.csv')

pepsu = pd.read_csv(file_path + '/merge_10_state/pepsu_bus_data.csv')

rsrtc = pd.read_csv(file_path + '/merge_10_state/rsrtc_bus_data.csv')

south_bengal = pd.read_csv(file_path + '/merge_10_state/south_bengal_bus_data.csv')

telangana = pd.read_csv(file_path + '/merge_10_state/telangana_bus_data.csv')

up = pd.read_csv(file_path + '/merge_10_state/up_bus_data.csv')

west_bengal = pd.read_csv(file_path + '/merge_10_state/west_bengal_bus_data.csv')

# print(chand.head())

ap['state'] = 'Andhra Pradesh'
ap.to_csv('andhra_bus_data.csv', index=False)

chand['state'] = 'Chandigarh'  # Replace 'your_value' with the desired value
chand.to_csv('chandigarh_bus_data.csv', index=False)

himachal['state'] = 'Himachal Predesh'
himachal.to_csv('himachal_bus_data.csv', index = False)

kerala['state'] = 'Kerala'
kerala.to_csv('kerala_bus_data.csv', index=False)

pepsu['state'] = 'pepsu'
pepsu.to_csv('pepsu_bus_data.csv', index=False)

rsrtc['state'] = 'rsrtc'
rsrtc.to_csv('rsrtc_bus_data.csv', index=False)

south_bengal['state'] = 'south_bengal'
south_bengal.to_csv('south_bengal_bus_data.csv', index=False)

telangana['state'] = 'telangana'
telangana.to_csv('telangana_bus_data.csv', index=False)

up['state'] = 'up'
up.to_csv('up_bus_data.csv', index=False)

west_bengal['state'] = 'west_bengal'
west_bengal.to_csv('west_bengal_bus_data.csv', index=False)

print("success")