import csv

file_name = str(input('Enter the name of the csv file without extension (.csv)>>> '))
col_num = int(input('Enter the number of columns: '))
row_num = int(input('Enter the number of rows: '))
with open(f'{file_name}.csv', 'w') as csv_file:
        print('\nEnter Headers: \n')
        for _ in range(col_num):
                csv.writer.writerow(str(input('>'))+'\n')
                
        print('\nEnter rows: \n')
        for _ in range(row_num):
                csv_file.writer.writerow(str(input('>'))+'\n')
