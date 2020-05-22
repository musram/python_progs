import csv


def reader(filename):

    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            yield row

def process_data(region, rows):
    for row in rows:
        if row[-1] == region:
            print(row)
    


if __name__ == "__main__":

    
        
    rows = reader('./data-1-master/thanksgiving-2015/thanksgiving-2015-poll-data.csv')

    print(next(rows))
    print(next(rows))


    process_data('Middle Atlantic', rows)

    
