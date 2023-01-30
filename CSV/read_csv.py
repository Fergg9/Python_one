import csv

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        print(header)
        '''for row in reader:
            print('****' * 30)
            print(row)'''
            
if __name__ == '__main__':
    read_csv('/home/fergg/py_project/CSV/data.csv')  
              