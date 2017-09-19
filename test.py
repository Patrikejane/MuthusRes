import time
import stringcmp

__author__ = 'sunimal.malkakulage'

with open('TEST_DATA.csv', 'rb') as f_open:
    msg = []
    # data =  [line.rstrip('\n\r').split(',') for line in f_open]

    for line in f_open:
        twoNames = line.rstrip('\n\r').split(',')
        print(twoNames)
        s = '%13s,%13s,' % (twoNames[0], twoNames[1])

        ##------Jaro------##
        start_time = time.time()
        s += ' %.3f' % (stringcmp.jaro(twoNames[0], twoNames[1]))
        time_used = time.time() - start_time
        s += ' %.10f' % (time_used)

        ##------winkler------##
        start_time1 = time.time()
        s += ' %.3f' % (stringcmp.winkler(twoNames[0], twoNames[1]))
        time_used1 = time.time() - start_time1
        s += ' %.10f' % (time_used1)

        ##------qgram 1------##
        start_time2 = time.time()
        s += ' %.3f' % (stringcmp.qgram(twoNames[0], twoNames[1], 1))
        time_used2 = time.time() - start_time2
        s += ' %.10f' % (time_used2)

        ##------qgram 2------##
        start_time3 = time.time()
        s += ' %.3f' % (stringcmp.qgram(twoNames[0], twoNames[1], 2))
        time_used3 = time.time() - start_time3
        s += ' %.10f' % (time_used3)

        ##------qgram 3------##
        start_time4 = time.time()
        s += ' %.3f' % (stringcmp.qgram(twoNames[0], twoNames[1], 3))
        time_used4 = time.time() - start_time4
        s += ' %.10f' % (time_used4)

        ##------posqgram 1------##
        start_time5 = time.time()
        s += ' %.3f' % (stringcmp.posqgram(twoNames[0], twoNames[1], 1))
        time_used5 = time.time() - start_time5
        s += ' %.10f' % (time_used5)

        ##------posqgram 2------##
        start_time6 = time.time()
        s += ' %.3f' % (stringcmp.posqgram(twoNames[0], twoNames[1], 2))
        time_used6 = time.time() - start_time6
        s += ' %.10f' % (time_used6)

        ##------posqgram 3------##
        start_time7 = time.time()
        s += ' %.3f' % (stringcmp.posqgram(twoNames[0], twoNames[1], 3))
        time_used7 = time.time() - start_time7
        s += ' %.10f' % (time_used7)


        ##------sgram------##
        start_time8 = time.time()
        s += ' %.3f' % (stringcmp.sgram(twoNames[0], twoNames[1], [[0], [0, 1], [1, 2]]))
        time_used8 = time.time() - start_time8
        s += ' %.10f' % (time_used8)

        ##------editdist------##
        start_time9 = time.time()
        s += ' %.3f' % (stringcmp.editdist(twoNames[0], twoNames[1]))
        time_used9 = time.time() - start_time9
        s += ' %.10f' % (time_used9)

        ##------mod_editdist------##
        start_time10 = time.time()
        s += ' %.3f' % (stringcmp.mod_editdist(twoNames[0], twoNames[1]))
        time_used10 = time.time() - start_time10
        s += ' %.10f' % (time_used10)

        ##------bagdist------##
        start_time11 = time.time()
        s += ' %.3f' % (stringcmp.bagdist(twoNames[0], twoNames[1]))
        time_used11 = time.time() - start_time11
        s += ' %.10f' % (time_used11)

        ##------editex------##
        start_time12 = time.time()
        s += ' %.3f' % (stringcmp.editex(twoNames[0], twoNames[1]))
        time_used12 = time.time() - start_time12
        s += ' %.10f' % (time_used12)

        ##------seqmatch------##
        start_time13 = time.time()
        s += ' %.3f' % (stringcmp.seqmatch(twoNames[0], twoNames[1]))
        time_used13 = time.time() - start_time13
        s += ' %.10f' % (time_used13)

        ##------compression bz2 ------##
        start_time14 = time.time()
        s += ' %.3f' % (stringcmp.compression(twoNames[0], twoNames[1], 'bz2'))
        time_used14 = time.time() - start_time14
        s += ' %.10f' % (time_used14)

        ##------compression zlib ------##
        start_time15 = time.time()
        s += ' %.3f' % (stringcmp.compression(twoNames[0], twoNames[1], 'zlib'))
        time_used15 = time.time() - start_time15
        s += ' %.10f' % (time_used15)

        ##------compression arith ------##
        start_time16 = time.time()
        s += ' %.3f' % (stringcmp.compression(twoNames[0], twoNames[1], 'arith'))
        time_used16 = time.time() - start_time16
        s += ' %.10f' % (time_used16)

        ##------lcs 2 ------##
        start_time17 = time.time()
        s += ' %.3f' % (stringcmp.lcs(twoNames[0], twoNames[1], 2))
        time_used17 = time.time() - start_time17
        s += ' %.10f' % (time_used17)

        ##------lcs 3 ------##
        start_time18 = time.time()
        s += ' %.3f' % (stringcmp.lcs(twoNames[0], twoNames[1], 3))
        time_used18 = time.time() - start_time18
        s += ' %.10f' % (time_used18)

        ##------ontolcs 2 ------##
        start_time19 = time.time()
        s += ' %.3f' % (stringcmp.ontolcs(twoNames[0], twoNames[1], 2))
        time_used19 = time.time() - start_time19
        s += ' %.10f' % (time_used19)

        ##------ontolcs 3 ------##
        start_time20 = time.time()
        s += ' %.3f' % (stringcmp.ontolcs(twoNames[0], twoNames[1], 3))
        time_used20 = time.time() - start_time20
        s += ' %.10f' % (time_used20)

        ##------permwinkler ------##
        start_time21 = time.time()
        s += ' %.3f' % (stringcmp.permwinkler(twoNames[0], twoNames[1]))
        time_used21 = time.time() - start_time21
        s += ' %.10f' % (time_used21)

        ##------sortwinkler ------##
        start_time22 = time.time()
        s += ' %.3f' % (stringcmp.sortwinkler(twoNames[0], twoNames[1]))
        time_used22 = time.time() - start_time22
        s += ' %.10f' % (time_used22)

        ##------swdist ------##
        start_time23 = time.time()
        s += ' %.3f' % (stringcmp.swdist(twoNames[0], twoNames[1]))
        time_used23 = time.time() - start_time23
        s += ' %.10f' % (time_used23)

        ##------syllaligndist ------##
        start_time24 = time.time()
        s += ' %.3f' % (stringcmp.syllaligndist(twoNames[0], twoNames[1]))
        time_used24 = time.time() - start_time24
        s += ' %.10f' % (time_used24)

        ##------charhistogram ------##
        start_time25 = time.time()
        s += ' %.3f' % (stringcmp.charhistogram(twoNames[0], twoNames[1]))
        time_used25 = time.time() - start_time25
        s += ' %.10f' % (time_used25)

        ##------twoleveljaro ------##
        start_time26 = time.time()
        s += ' %.3f' % (stringcmp.twoleveljaro(twoNames[0], twoNames[1]))
        time_used26 = time.time() - start_time26
        s += ' %.10f' % (time_used26)

        ##------twoleveljaro with threhold ------##
        start_time27 = time.time()
        s += ' %.3f' % (stringcmp.twoleveljaro(twoNames[0], twoNames[1], stringcmp.qgram, 0.8))
        time_used27 = time.time() - start_time27
        s += ' %.10f' % (time_used27)

        # print(s)
        msg.append(s)

        if (stringcmp.qgram(twoNames[0], twoNames[1], 2) != stringcmp.sgram(twoNames[0], twoNames[1], gc=[[0]])):
            msg.append('  Error: 2-gram != s-gram (with gc=[[0]])')
        if (stringcmp.editdist(twoNames[0], twoNames[1]) > stringcmp.bagdist(twoNames[0], twoNames[1])):
            msg.append('  Error: BadD > EditD')

        if (stringcmp.lcs(twoNames[0], twoNames[1], 1) < stringcmp.lcs(twoNames[0], twoNames[1], 2)):
            msg.append('  Error: LCS1 < LCS2')

        if (stringcmp.lcs(twoNames[0], twoNames[1], 2) < stringcmp.lcs(twoNames[0], twoNames[1], 3)):
            msg.append('  Error: LCS2 < LCS3')

        if (stringcmp.editdist(twoNames[0], twoNames[1]) > stringcmp.mod_editdist(twoNames[0], twoNames[1])):
            msg.append('  Error: EditD > Modified EditD')

    print(msg)

f = open('MyResult.csv', 'w')
#print(len(msg))
count = 0
for i in msg:
    count += 1
    csResults = i.split(',')
    finalCsResalt = csResults[0] + ',' + csResults[1] + ','.join(csResults[2].split(' '))
    # print(m)
    #print(count)
    f.write(finalCsResalt)
    f.write('\n')
f.close()


def classifier_performance(tp, fp, tn, fn):
    #sensitivity = (float(tp) / (tp + fn)) * 100
    #specificity = (float(tn) / (fp + tn)) * 100
    precision = (float(tp) / (tp + fp)) * 100
    accuracy = (float(tp + tn) / (tp + fp + tn + fn)) * 100
    print "accuracy =", round(accuracy, 3), "precision =", round(precision, 3)