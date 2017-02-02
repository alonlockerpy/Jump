s = "fname:John,lname:doe,mname:dunno,city:Florida"
sd = dict(u.split(":") for u in s.split(","))
for value in sd.values():
    print "test: " + value