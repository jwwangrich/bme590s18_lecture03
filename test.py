from glob import glob
    with open('everyone.csv', 'a') as singleFile:
         for csv in glob('*.csv'):
            if csv == 'mlp6.csv':
                pass
            else:
                for line in open(csv, 'r'):
                    singleFile.write(line)

                    pass



csvfile = open('*.csv', 'r')
    jsonfilename = files
    jsonfile = open('*.json', 'w')
    reader = csv.reader(csvfile)




json_data = json.dumps(data)
    csv_rows.extend([{field[i]: row[field[i]] for i in range(len(field))}])
    convert_write_json(csv_rows, json_file)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')


global rd2
    data = rd2
    data.append()
    json_data = json.dumps(data)



csvfile = open(filename,"r")
    temp = list(csv.reader(csvfile,delimiter=","))
    json_filename = filename.replace('.csv','.json')
    json_file = open(json_filename, "w")
    json_file.write(",".join(temp[0]))
    json_file.close