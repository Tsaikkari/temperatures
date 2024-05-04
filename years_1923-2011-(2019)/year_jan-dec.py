import csv
import json

# _0 and _12 files data preparation and printing of annual average temperatures per month for multiple stations

def get_temperatures(files):
    number_of_files = len(files)
    combined_annual_avg_temperatures = [] # list of year/average temperature objects combined of multiple files
    station_data = {} # 'uncleaned' station object that includes montly average temperature list where years are the keys
    temp_dict = {} # one (the first station) 'cleaned' object that includes annual average temperatures for the station
    annual_avg_temperature_list = [] # a list of {'year': XXXX, 'temperature': xx.xx} objects of station data

    for filename in files:
        with open(filename) as new_file:
            for line in new_file:
                line = line.replace(' ', ',')
                line = line.strip()
                row = line.split(',')
                if row[0] == 'YEAR':
                    continue
                year = row[0]
                if year == '':
                    continue
                station_data[year] = []
                for temperature in row[1:]:
                    if temperature != '':
                        station_data[year].append(float(temperature)) 
        
        calc_average_monthly_temp(station_data, annual_avg_temperature_list, temp_dict)

    if number_of_files > 1: 
        for year, _ in temp_dict.items():
            summe = 0
            for row in annual_avg_temperature_list:
                if year == row['year']:
                    summe += float(row['temperature'])
            combined_annual_avg_temperatures.append({'year': year, 'temperature': round(summe / number_of_files, 2)})
        return [combined_annual_avg_temperatures, number_of_files]
    return annual_avg_temperature_list

def calc_average_monthly_temp(station_data: object, annual_avg_temperature_list: list, temp_dict: object):
    for year, temperatures in station_data.items():
        temperatures = temperatures[:-5]
        # TODO: maybe change this
        if 999.9 in temperatures:
            continue
        if len(temperatures) > 0:
            average = sum(temperatures) / len(temperatures)
            annual_avg_temperature_list.append({'year': int(year), 'temperature': round(average, 2)})
            temp_dict[int(year)] = average
    return [annual_avg_temperature_list, temp_dict]

def print_to_csv(data: list):
    array = []

    for row in data[0]:
        array.append([row['year'], row['temperature']])
    with open(f"outfile_0({data[1]}).csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(array)

def print_to_json(data: list):
    with open(f"data_0.json", 'w') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)
        
#results_12 = get_temperatures(['Vardo_0.txt', 'Sodankyla_0.txt', 'Malye_Karmaku_0.txt'])
results = get_temperatures(['Vardo_0.txt', 'Sodankyla_0.txt', 'Malye_Karmaku_0.txt'])
#print_to_csv(results_12)
print_to_csv(results)

#print_to_json(results[0])
#print_to_json(results_12[0])




