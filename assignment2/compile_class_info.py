import glob
import csv
import json

teamname = ""
csvsinglefile = ""
data = ""
rd2 = ""
files = ""

def main():
    collect_all_csv_filenames()
    global files
    global teamname
    with open('everyone.csv', 'a') as csvfile:
        f = csv.writer(csvfile, delimiter = ',')
        for files in csvsinglefile:
           if files != 'mlp6.csv':
                rd = csv.reader(open(files, 'r'),delimiter = ',')
                rd2 = list(csv.reader(open(files, 'r'),delimiter = ','))
                teamname = rd2[0][4]
                for row in rd:
                    f.writerow(row)
                    read_csv()
                    write_data()


def collect_all_csv_filenames():
    global csvsinglefile
    csvsinglefile = glob.glob('*.csv')
    #f = csv.writer(open('everyone.csv', 'a'), delimiter = ',')




def read_csv():
    check_no_spaces()

    check_camel_case()



def write_data(type='json'):
    global files
    csvfiles = open(files, "r")
    temp = list(csv.reader(csvfiles, delimiter=","))
    json_filename = files.replace('.csv', '.json')
    json_file = open(json_filename, "w")
    json_file.write(",".join(temp[0]))



def check_no_spaces():
        global teamname
        t = 0
        if teamname == " " :
           t = t + 1
           print(t)
        else:
            return print(t)



def check_camel_case():
    global teamname
    s = teamname
    p = 0
    if (s != s.lower() and s != s.upper()) :
      p = p + 1
      return print(p)






if __name__ == "__main__":
    main()