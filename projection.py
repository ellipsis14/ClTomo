import cv2
import numpy as np

def projections(IMG, THETA):
    iLength, iWidth = IMG.shape
    iDiag = np.sqrt(iLength**2 + iWidth**2)
    LengthPad = int(np.ceil(iDiag - iLength) + 2)
    WidthPad = int(np.ceil(iDiag - iWidth) + 2)
    padIMG = np.pad(IMG, ((int(LengthPad/2), int(LengthPad/2)), (int(WidthPad/2), int(WidthPad/2))), 'constant')

    n = len(THETA)
    PR = np.zeros((padIMG.shape[1], n))
    for i in range(n):
        tmpimg = cv2.rotate(padIMG, cv2.ROTATE_90_CLOCKWISE)
        PR[:, i] = np.sum(tmpimg, axis=0)
        print(THETA[i])
    return PR
