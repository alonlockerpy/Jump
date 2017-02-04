
class txt:
    # Example for read txt file, split to make list of rows print data.
    def stringtest(self):
        with open('test.txt') as file:
            print "Here are your tasks:"
            for line in file.readlines():
                arry = line.split(";")
                date = arry[0]
                task = arry[2]
                print date, task
        file.close()

    # Example for read txt split to dictnery, get valus of keys
    def stringsplit(self):
        s = "fname:John,lname:doe,mname:dunno,city:Florida"
        sd = dict(u.split(":") for u in s.split(","))
        for value in sd.values():
            print "The team members are: " + value


txt1 = txt()
txt1.stringtest()
txt1.stringsplit()


