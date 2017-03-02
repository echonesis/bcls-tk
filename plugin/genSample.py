import sys
import argparse

if __name__ == '__main__':
    # Parser Settings
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="Dummy row number")
    parser.add_argument("-o", "--output", help="Output file")
    args = parser.parse_args()

    # Input Settings
    """
    rowNum = sys.argv[2]
    outputFile = sys.argv[1]
    """
    rowNum = int(args.number)
    outputFile = args.output

    targetStr = "Yield"
    for i in range(1000):
        targetStr = targetStr + ",10"

    f = open(outputFile, 'w')
    for i in range(rowNum):
        f.write(targetStr + '\n')
    f.close()

    print "[Status] End of sample file generation.\n"
