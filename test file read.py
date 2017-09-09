with open('file.csv','rb') as f_open:
    data =  [line.split(',')[0:2] for line in f_open]
    data2 =  [line.split(',')[1] for line in f_open]

    data2 = [arr[0]+ ' ' +arr[1] for arr in data]

print data2
