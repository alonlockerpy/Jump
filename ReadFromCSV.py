import csv


def setUp():
    with open('cars.csv') as f:
        d = dict(filter(None, csv.reader(f)))
        print d


setUp()