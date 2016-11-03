import numpy as np
import matplotlib.pyplot as plt

from skimage.transform import radon
from scipy.spatial.distance import cosine as distcosine

def genRadonProfile(M, A=4):
    theta = np.linspace(0., 180., A, endpoint=False)
    signal = radon(M, theta, circle=False)
    result = signal.flatten('F')
    return result

def genRadonDistance(M1, M2):
    profile1 = genRadonProfile(M1)
    profile2 = genRadonProfile(M2)
    result = distcosine(profile1, profile2)
    return result
    

if __name__ == '__main__':
    A = np.array([[1, 1], [1, 0]])
    B = np.array([[1, 0], [1, 0]])
    result = genRadonDistance(A, B)
    print('Modified Distance:', result)
