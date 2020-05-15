import json 
import csv
from .appl import l

with open('data.json','w') as json_file: 
    json.dump(l, json_file) 


with open('data.json') as json_file: 
    data = json.load(json_file) 
  
data = data
  
data_file = open('data_file.csv', 'w') 
  
csv_writer = csv.writer(data_file) 

count = 0
  
for da in data: 
    if count == 0: 
 
        header = da.keys() 
        csv_writer.writerow(header) 
        count += 1
 
    csv_writer.writerow(da.values()) 
  
data_file.close()