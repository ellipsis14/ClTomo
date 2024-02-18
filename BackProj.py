    """
    This function implements filtered back projection 
    Returns:
        _type_: _description_
    """
import cv2
import numpy as np

def backproject3(PR, THETA):
    n = PR.shape[0]
    sideSize = n

    # filter the projections
    filtPR = projfilter(PR)

    # convert THETA to radians
    th = (np.pi/180) * THETA

    # set up the image
    m = len(THETA)
    BPI = np.zeros((sideSize, sideSize))

    # find the middle index of the projections
    midindex = (n + 1) // 2

    # set up x and y matrices
    x = np.arange(sideSize)
    y = np.arange(sideSize)
    X, Y = np.meshgrid(x, y)
    xpr = X - (sideSize + 1) / 2
    ypr = Y - (sideSize + 1) / 2

    for i in range(m):
        print('On angle', THETA[i])
        filtIndex = np.round(midindex + xpr * np.sin(th[i]) - ypr * np.cos(th[i])).astype(int)
        BPIa = np.zeros((sideSize, sideSize))
        spota = np.where((filtIndex > 0) & (filtIndex <= n))
        newfiltIndex = filtIndex[spota]
        BPIa[spota] = filtPR[newfiltIndex, i]
        BPI += BPIa

    BPI /= m
    return BPI
