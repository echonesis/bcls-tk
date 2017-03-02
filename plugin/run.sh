#!/bin/sh

python genSample.py -o TestSample.data -n 100
python trMat.py -i TestSample.data
