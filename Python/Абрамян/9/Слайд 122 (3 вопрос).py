import datetime as d
td = d.datetime.now()
birth = d.datetime.strptime("2008-5-5","%Y-%m-%d")
a = (td - birth).days
print(a)