import csv
import os

def read_csv(file_dir, file_name):
    file_path = file_dir + file_name
    if not os.path.isfile(file_path):
        return []

    with open(file_path) as f:
        dict_reader = csv.DictReader(f)
        csv_file = [row for row in dict_reader]

    return csv_file

def update_csv(file_dir, file_name, rowdata):
    file_path = file_dir + file_name

    header = rowdata[0].keys()
    print(header)

    with open(file_path, mode='w', newline="") as f:
        # headerも渡してやる
        # 渡した順番が列の順番になる
        csvout = csv.DictWriter(f, header)
        csvout.writeheader()
        csvout.writerows(rowdata)

if __name__ == "__main__":
    val = read_csv("C:/Users/Owner/Documents/bingo/server/database/", "bingo_manage.csv")
    print(val)

    val[0]['len'] = 'bbb'
    print(val)
    update_csv("C:/Users/Owner/Documents/bingo/server/database/", "bingo_manage.csv", val)
