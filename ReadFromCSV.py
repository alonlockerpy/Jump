import csv
import pandas

def readCSV():
    with open('cars.csv') as f:
        d = filter(None, csv.reader(f))
        print d
        dd = {}
        #for test in d.values():
        #    print "test: " + test
        for key, val in d:
            stak = dd.setdefault(key, []).append(val)
            for test in stak.values():
                print "test: " + test
readCSV()

def pandastest():
    df = pandas.read_csv('cars.csv')
    print 'test'
#pandastest()

my_dict = {'name': 'ed', 'age': 40, 'hobby': 'run'}
import json

json.dumps(my_dict)
with open('my_dict.json', 'w') as fp:
    json.dump(my_dict, fp)
    fp.close()


with open('my_dict.json') as fp:
    x =  json.load( fp)
    fp.close()


# read and parse logs
# import glob
# for f_name in glob.glob('c: .log'):
#     print f_name

#Function that gets lof file value, read its lines and look for a value, print that liens
def readLog(logFile):
    count = 0
    with open(f_name) as fp:
          for line in fp.readlines():
            if line.find('2015') >= 0:
                print line
                count += 1
          print "Found",count,"results."

    fp.close()


    start=1
    step=1
    print(list(range(start, 14, step)))

#f_name = 'c:\\test.log'
#readLog(f_name)
