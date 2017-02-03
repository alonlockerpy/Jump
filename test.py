#s = "fname:John,lname:doe,mname:dunno,city:Florida"
#sd = dict(u.split(":") for u in s.split(","))
#for value in sd.values():
#    print "test: " + value


def stringtest():
    with open('test.txt') as file:
        print "Here are your tasks:"
        for line in file.readlines():
            arry = line.split(";")
            date = arry[0]
            task = arry[2]
            print date, task
    file.close()

stringtest()
    #dic[arry[4]] = arry[0]
    #dic with more then one value

