import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2018-10-12T4:45:52', format)
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))
t2 = dt.datetime.now()
diff = t2 - t1
print('Số ngày chênh lệch: ' + str(diff.days))