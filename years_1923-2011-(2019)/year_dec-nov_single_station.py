import csv
import json

# ds=0 and ds=12 files of v2 data preparation and printing of annual average temperatures per month for a station

def get_temperatures(file):
    station_data = {} # station object that includes montly average temperature lists where years are the keys
    annual_avg_temperatures = [] # a list of {'year': XXXX, 'temperature': xx.xx} objects of station data

    with open(file) as new_file:
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
    return [annual_avg_temperatures, file]
             
#     get_dec_nov_year_avg(station_data, data_mix, annual_avg_temperatures)
  
#     if number_of_files > 1: 
#         for year, _ in data_mix.items():
#             summe = 0
#             for row in annual_avg_temperatures:
#                 if year == row['year']:
#                     summe += float(row['temperature'])
#             combined_annual_avg_temperatures.append({'year': year, 'temperature': round(summe / number_of_files, 2)})
#         return [combined_annual_avg_temperatures, number_of_files]
#     return [annual_avg_temperatures, 1]

# def get_dec_nov_year_avg(station_data: object, data_mix: object, annual_average_temperatures: list):
#     last_in_list = 0
#     start_year = '1923'
    
#     for year, temperatures in station_data.items():
#         temperature_list = temperatures[:-5]
#         # TODO: maybe change this
#         if 999.9 in temperature_list:
#             continue
#         if year == start_year:
#             if temperature_list != []:
#                 last_in_list = temperature_list.pop(-1)
#                 continue
#         if temperature_list != []:
#             year = int(year) 
#             data_mix[year] = []
#             temperature_list.insert(0, last_in_list)
#             data_mix[year].append(temperature_list)
#             last_in_list = temperature_list.pop(-1)
    
#     for year, temperatures in data_mix.items():
#         for temperature_list in temperatures:
#             average = round(sum(temperature_list) / len(temperature_list), 2)
#         annual_average_temperatures.append({'year': year, 'temperature': average})

#     return [annual_average_temperatures, data_mix]

def print_to_csv(data: list):
    array = []

    for row in data[0]:
        array.append([row['year'], row['temperature']])
    with open(f"outfile_0_dec-nov({data[1]}).csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(array)

def print_to_json(data: list):
    with open(f"data_0_dec-nov_{data[1]}", 'w') as f:
       json.dump(data[0], f, ensure_ascii=False, indent=4)
        
# results_12 = get_temperatures([
#     'Vardo_12.txt', 
#     'Sodankyla_12.txt', 
#     'Malye_Karmaku_12.txt', 
#     'Bodo_Vi_12.txt', 
#     'Jan_Mayen_12.txt', 
#     'Karajok_12.txt', 
#     'Tromo-Skatto_Norway_12.txt'
# ])

results = get_temperatures('Vardo_0.txt')

#print_to_csv(results_12)
#print_to_csv(results)

print_to_json(results)
#print_to_json(results_12[0])



