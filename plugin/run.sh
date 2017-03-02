#!/bin/sh

python genSample.py TestSample.data 1000000
python trMat.py TestSample.data
