import numpy as np
import math

def getSelectedWindow(obj, thr):
    mu_x = obj[0][0]
    mu_y = obj[0][1]
    std_x = obj[1][0]
    std_y = obj[1][1]
    x_start = math.floor(mu_x - thr*std_x)
    x_end = math.ceil(mu_x + thr*std_x)
    y_start = math.floor(mu_y - thr*std_y)
    y_end = math.ceil(mu_y + thr*std_y)
    return [(x_start, x_end), (y_start, y_end)]

def getGravity(x):
    xlist = list()
    ylist = list()
    for obj in x:
        xlist.append(obj[0])
        ylist.append(obj[1])
    mu_x = np.mean(xlist)
    mu_y = np.mean(ylist)
    std_x = np.std(xlist)
    std_y = np.std(ylist)
    return [(mu_x, mu_y), (std_x, std_y)]

if __name__ == "__main__":
    selectTerm = input('Please select your target test: (1:Gravity)')
    print('Selected Term:', selectTerm)
    
    if int(selectTerm) == 1:
        testList = [(0, 0), (5, 0), (1, 5), (6, 5)]
        result = getGravity(testList)
        print('mu:', result[0])
        print('std:', result[1])

    else:
        print('Not supported test.')
