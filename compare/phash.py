import numpy as np

def genPHashDist(A, B):
    rMat = A - B
    boolMat = np.nonzero(rMat)
    acc = 1 - len(boolMat[0]) / (A.shape[0] * A.shape[1])
    #print('Accuracy:', acc)
    return 1 - acc**2

if __name__ == '__main__':
    A = np.matrix([[1, 1], [1, 1]])
    B = np.matrix([[1, 1], [2, 1]])
    result = genPHashDist(A, B)
    print('pHash Dist:', result)
