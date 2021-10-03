time = float(input('Enter Time in Seconds : '))
day = time // (24 * 3600)
time = time % (24 * 3600)
hr = time // 3600
time %= 3600
mins = time // 60
time %= 60
secs = time

print('D:H:M:S-> %d:%d:%d:%d' % (day, hr, mins, secs))
print('Day\t\t: ',day)
print('Hour\t: ',hr)
print('Minutes : ',mins)
print('Seconds : ',secs)