import json

# ds=0 and ds=12 files of v2 data preparation and printing of annual average temperatures per month for multiple stations

def get_temperatures(files):
    annual_avg_temperatures = [] # a list of arrays 

    for filename in files:
        with open(filename) as new_file:
            for line in new_file:
                line = line.strip()
                row = line.split(',')
                year = row[0]
                if year != '':
                    annual_avg_temperatures.append({'year': year, 'temperature': row[1]})
                
                    sum_temperatures = 0
                    count = 0
                    for item in annual_avg_temperatures:
                        if year == item['year']:
                            count += 1
                            sum_temperatures = sum_temperatures + float(item['temperature'])
                            average = sum_temperatures / len(files)
                            if count == len(files):
                                item['temperature'] = round(average, 2)
    if annual_avg_temperatures[-1]['year'] == '':
        annual_avg_temperatures.pop(-1)
    nominator = len(files)
    index = len(annual_avg_temperatures) - (len(annual_avg_temperatures) / nominator) 
    index = round(index)
    return annual_avg_temperatures[index:]

def print_to_json(data: list):
    with open(f"data_0_dec-nov.json", 'w') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)
        
results = get_temperatures([
    'outfile_dec-nov(Vardo_0).csv', 
    'outfile_dec-nov(Sodankyla_0).csv', 
    'outfile_dec-nov(Bodo_Vi_0).csv',
    'outfile_dec-nov(Jan_Mayen_0).csv', 
    'outfile_dec-nov(Malye_Karmaku_0).csv', 
    'outfile_dec-nov(Karajok_0).csv', 
    'outfile_dec-nov(Tromo-Skatto_Norway_0).csv' 
])

print_to_json(results)
#print_to_json(results_12)




