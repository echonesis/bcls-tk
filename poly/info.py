import numpy as np


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
