import csv
import json

# _0 and _12 files data preparation and printing of annual metANN temperatures per month for multiple stations

def get_temperatures_with_modified_avg_data(files):
    number_of_files = len(files)
    year_metANN = []
    temp_dict = {}
    year_metANN_multi_stations = []

    for filename in files:
        with open(filename) as new_file:
            for line in new_file:
                line = line.replace(' ', ',')
                line = line.strip()
                row = line.split(',')
                if row[0] == 'YEAR':
                    continue
                if row[-1] != '':
                    year_metANN.append({'year': int(row[0]), 'temperature': float(row[-1])})
                    temp_dict[int(row[0])] = row[-1]
    
    if number_of_files > 1: 
        for key, _ in temp_dict.items():
            summe = 0
            for record in year_metANN:
                if key == record['year']:
                    summe += float(record['temperature']) 
            average = summe / number_of_files
            year_metANN_multi_stations.append({'year': key, 'temperature': round(average, 2)})
        return year_metANN_multi_stations 
    return year_metANN

def print_to_csv(data):
    array = []
    for row in data:
        array.append([row['year'], row['temperature']])

    with open("outfile_00.csv", 'w') as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(('year', 'avg'))
        writer.writerows(array)

def print_to_json(data: list):
    with open("data_00.json", 'w') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)

results = get_temperatures_with_modified_avg_data(['Vardo_0.txt', 'Sodankyla_0.txt'])
results_12 = get_temperatures_with_modified_avg_data(['Vardo_12.txt', 'Sodankyla_12.txt'])
print_to_csv(results)
#print_to_csv(results_12)

print_to_json(results)
#print_to_json(results_12)

