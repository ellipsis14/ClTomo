"""
    This function takes the image matrix and vector of angles and then 
finds the 1D projection (Radon transform) at each of the angles.  

    Returns: 
    It returns a matrix whose columns are the projections at each angle.
"""
import numpy as np
from scipy import ndimage

def proj(IMG, N):
    # Create a vector of values for theta
    interval = np.linspace(0, 180, N, endpoint=False)

    # Take images and pad with zero to eliminate error
    padIMG = np.pad(IMG, ((1, 1), (1, 1)), mode='constant')

    # Here we rotate the image N different angles of theta, and then sum the columns
    # of each of these projected images in order to build N different projections
    n = len(interval)
    Projection = np.zeros((padIMG.shape[1], n))
    for i in range(n):
        temp = ndimage.rotate(padIMG, interval[i], reshape=False)
        Projection[:, i] = np.sum(temp, axis=0)

    return Projection