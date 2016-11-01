import numpy as np
import math
import multiprocessing as mul

def genGaussianPdf(x, std, mu=0):
    result = 1 / std / (math.sqrt(2 * math.pi)) * math.exp(-1 * (x-mu)** 2 / (2 * std**2))
    return result

def genGaussianPdfWindow(W, std_pair):
    x_start = W[0][0]
    x_end = W[0][1]
    y_start = W[1][0]
    y_end = W[1][1]
    std_x = std_pair[0]
    std_y = std_pair[1]

    x_pos_mat = np.zeros(shape=(y_end-y_start+1, x_end-x_start+1))
    for iCol in range(x_pos_mat.shape[1]):
        for iRow in range(x_pos_mat.shape[0]):
            x_pos_mat[iRow, iCol] = iCol
    x_pos_mat = x_pos_mat - (x_end-x_start+1)/2 * np.ones(shape=(y_end-y_start+1, x_end-x_start+1))
    y_pos_mat = np.zeros(shape=(y_end-y_start+1, x_end-x_start+1))
    for iCol in range(x_pos_mat.shape[1]):
        for iRow in range(x_pos_mat.shape[0]):
            y_pos_mat[iRow, iCol] = iRow
    y_pos_mat = y_pos_mat - (y_end-y_start+1)/2 * np.ones(shape=(y_end-y_start+1, x_end-x_start+1))
    result_x_mat = np.zeros(shape=(y_end-y_start+1, x_end-x_start+1))
    result_y_mat = np.zeros(shape=(y_end-y_start+1, x_end-x_start+1)) 

    for iCol in range(x_pos_mat.shape[1]):
        for iRow in range(x_pos_mat.shape[0]):
            result_x_mat[iRow, iCol] = genGaussianPdf(x_pos_mat[iRow, iCol], std_x)
    print('Result X:', result_x_mat)

    for iCol in range(y_pos_mat.shape[1]):
        for iRow in range(y_pos_mat.shape[0]):
            result_y_mat[iRow, iCol] = genGaussianPdf(y_pos_mat[iRow, iCol], std_y)
    print('Result Y:', result_y_mat)


    result = result_x_mat * result_y_mat

    return result

if __name__ == '__main__':
    W = [(1, 10), (1, 5)]
    result = genGaussianPdfWindow(W, (1, 1))
    print('Result:', result)
