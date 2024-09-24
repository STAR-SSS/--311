#повыш1
n = int(input())
min=n//60
ostatokmin=n%60
hour=min//60
ostatokhour=n%60
day=hour//24
ostatokday=n%24
print('minut',min,'sec',ostatokmin)
print('hour',hour,'min',ostatokhour)
print('day',day, 'hour',ostatokday)