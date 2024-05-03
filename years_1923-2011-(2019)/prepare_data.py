import csv

number_of_files = 0

def get_temperatures_with_modified_avg_data(files):
    number_of_files = len(files)
    lines = []
    map = {}
    result = []
    length = len(files)

    for filename in files:
        with open(filename) as new_file:
            for line in new_file:
                line = line.replace(' ', ',')
                line = line.strip()
                records = line.split(',')
                if records[0] == 'YEAR':
                    continue
                if records[-1] != '':
                    lines.append({'year': int(records[0]), 'temperature': float(records[-1])})
                    map[int(records[0])] = records[-1]
    
    if number_of_files > 1: 
        for key, value in map.items():
            value = float(value)
            for record in lines:
                if key == record['year']:
                    value += float(record['temperature']) 
                    result.append({'year': key, 'temperature': value / length})
                    map = {}
        return result 
    return lines

def print_to_csv(data):
    array = []
    if number_of_files > 1:
        cleaned = data[::2]
        for row in cleaned:
            array.append([row['year'], row['temperature']])

        with open("outfile_00.csv", 'w') as out_file:
            writer = csv.writer(out_file)
            # writer.writerow(('year', 'avg'))
            writer.writerows(array)
    for row in data:
        array.append([row['year'], row['temperature']])
        with open("outfile_00.csv", 'w') as out_file:
            writer = csv.writer(out_file)
            # writer.writerow(('year', 'avg'))
            writer.writerows(array)

results = get_temperatures_with_modified_avg_data(['Vardo_0.txt'])
#results_12 = get_temperatures(['Vardo_12.txt', 'Sodankyla_12.txt'])
print_to_csv(results)

