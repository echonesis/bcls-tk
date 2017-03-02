import sys
import numpy as np
import time

def read_in_bundle(inputFile, bNum=50):
    i = 0
    tmpMat = list()
    f = open(inputFile)
    for line in f:
        tmpLine = line.strip().split(',')
        tmpMat.append([x for x in tmpLine[1:len(tmpLine)]])

        if i % bNum == 0 and i > 0:
            # DANGEROUS
            resultMat = np.transpose(np.asarray(tmpMat, dtype=np.float32))
            tmpMat = []
            yield resultMat
    else:
        resultMat = np.transpose(np.asarray(tmpMat, dtype=np.float32))
        yield resultMat

    f.close()

if __name__ == '__main__':
    inputFile = sys.argv[1]
    time1 = time.time()
    matGen = read_in_bundle(inputFile)
    print 'Used Time:', time.time() - time1, '(s)'
    label = 0
    for i in matGen:
        if label == 0:
            result = i
            label += 1
        else:
            result = np.concatenate((result, i), axis=1)

    print('Dimension:', result.shape)

    print 'Used Time:', time.time() - time1, '(s)'
