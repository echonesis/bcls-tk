import sys

if __name__ == '__main__':
    rowNum = sys.argv[2]
    outputFile = sys.argv[1]

    targetStr = "Yield"
    for i in range(1000):
        targetStr = targetStr + ",10"

    f = open(outputFile, 'w')
    for i in range(int(rowNum)):
        f.write(targetStr + '\n')
    f.close()
