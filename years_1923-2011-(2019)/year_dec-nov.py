import csv
import json

# ds=0 and ds=12 files of v2 data preparation and printing of annual average temperatures per month for multiple stations

def get_temperatures(files):
    number_of_files = len(files)
    combined_annual_avg_temperatures = [] # list of year/average temperature objects combined of multiple files
    station_data = {} # 'uncleaned' station object that includes montly average temperature lists where years are the keys
    data_mix = {} # object of monthly average temperatures per year where year is the key
    annual_avg_temperatures = [] # a list of {'year': XXXX, 'temperature': xx.xx} objects of station data

    for filename in files:
        with open(filename) as new_file:
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
               
        get_dec_nov_year_avg(station_data, data_mix, annual_avg_temperatures)
  
    if number_of_files > 1: 
        for year, _ in data_mix.items():
            summe = 0
            for row in annual_avg_temperatures:
                if year == row['year']:
                    summe += float(row['temperature'])
            combined_annual_avg_temperatures.append({'year': year, 'temperature': round(summe / number_of_files, 2)})
        return [combined_annual_avg_temperatures, number_of_files]
    return annual_avg_temperatures

def get_dec_nov_year_avg(station_data: object, data_mix: object, annual_average_temperatures: list):
    last_in_list = 0
    start_year = '1923'
    
    for year, temperatures in station_data.items():
        temperature_list = temperatures[:-5]
        # TODO: maybe change this
        if 999.9 in temperature_list:
            continue
        if year == start_year:
            if temperature_list != []:
                last_in_list = temperature_list.pop(-1)
                continue
        if temperature_list != []:
            year = int(year) 
            data_mix[year] = []
            temperature_list.insert(0, last_in_list)
            data_mix[year].append(temperature_list)
            last_in_list = temperature_list.pop(-1)
    
    for year, temperatures in data_mix.items():
        for temperature_list in temperatures:
            average = round(sum(temperature_list) / len(temperature_list), 2)
        annual_average_temperatures.append({'year': year, 'temperature': average})
    print(data_mix)
    return [annual_average_temperatures, data_mix]

def print_to_csv(data: list):
    array = []

    for row in data[0]:
        array.append([row['year'], row['temperature']])
    with open(f"outfile_12_dec-nov({data[1]}).csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(array)

def print_to_json(data: list):
    with open(f"data_12_dec-nov.json", 'w') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)
        
results_12 = get_temperatures(['Vardo_12.txt', 'Sodankyla_12.txt', 'Malye_Karmaku_12.txt'])
#results = get_temperatures(['Vardo_0.txt', 'Sodankyla_0.txt', 'Malye_Karmaku_0.txt'])
#print(results)
#print_to_csv(results_12)
#print_to_csv(results)

#print_to_json(results[0])
#print_to_json(results_12[0])




