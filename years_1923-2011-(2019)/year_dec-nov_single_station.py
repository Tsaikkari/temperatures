import csv
import json

# ds=0 and ds=12 files of v2 data preparation and printing of annual average temperatures per month for a station

def get_temperatures(file):
    station_data = {} # station object that includes montly average temperature lists where years are the keys
    annual_avg_temperatures = [] # a list of {'year': XXXX, 'temperature': xx.xx} objects of station data
 
    with open(file) as new_file:
        print(file[:])
        start_year = '1923'
        last_in_list = 0
        for line in new_file:
            line = line.replace(' ', ',')
            line = line.strip()
            row = line.split(',')
            if row[0] == 'YEAR':
                continue
            year = row[0]
            station_data[year] = []
            for temperature in row[1:]:
                if temperature != '':
                    station_data[year].append(float(temperature))

            station_data[year] = station_data[year][:12]
            if station_data[year] != []:
                if year == start_year:
                    last_in_list = station_data[year].pop(-1)
                    station_data.pop('1923', None)  
                    continue
                station_data[year].insert(0, last_in_list)
                last_in_list = station_data[year].pop(-1)
               
            for year, temperatures in station_data.items():
                sum = 0
                average = 0
                for temperature in temperatures:
                    if temperature == 999.9:
                        continue
                    year = int(year)
                    sum += temperature
                    if len(temperatures) > 0:
                        average = sum / len(temperatures)
            annual_avg_temperatures.append({'year': year, 'temperature': round(average, 2)})
    return [annual_avg_temperatures[:-1], file]
             
def print_to_csv(data: list):
    array = []

    for row in data[0]:
        array.append([row['year'], row['temperature']])
    with open(f"outfile_dec-nov({data[1][:-4]}).csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(array)

def print_to_json(data: list):
    with open(f"data_dec-nov_{data[1][:-4]}.json", 'w') as f:
       json.dump(data[0], f, ensure_ascii=False, indent=4)
        
results = get_temperatures('Jan_Mayen_0.txt')

print_to_csv(results)
#print_to_json(results)





