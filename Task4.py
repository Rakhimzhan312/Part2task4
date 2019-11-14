time1=[int(input('Hours:')),int(input('Minute:')),int(input('Seconds:'))]
time2=[int(input('Hours:')),int(input('Minute:')),int(input('Seconds:'))]
if time1[0]==time2[0] and time1[1]==time2[1] and time1[2]==time2[2]:
    print('in time there is no difference')
else: 
    seconds=(time2[0]-time1[0])*3600+(time2[1]-time1[1])*60+(time2[2]-time1[2])
    print('Time difference:', seconds , 'seconds')
