import numpy as np
import matplotlib.pyplot as plt
import BackProj
import proj
import PIL.Image as img

def tomo(image, N):

    print('Loading Image into Python...')
    # Load image directly into NumPy array (assuming image loading mechanism is available)
    image_array = img.open(image)  # Replace with your image loading function

    # Plot the original image
    plt.figure(4)
    plt.gray() 
    plt.subplot(311)
    plt.imshow(image_array)
    plt.title('Original Picture')
    print('Plotting original image...')

    # Calculate projections
    interval = np.linspace(1, 180, N)
    Proj = proj(image_array, N)  
    print('Calculating projections of the image...')
    plt.subplot(312)
    plt.imshow(Proj)
    plt.title('Sinugram - Plot of unchanged Projections')

    # Add noise to projections (vectorized)
    print('Adding noise to each projection...')
    X = np.random.randn(144)
    Proj = Proj + 2 * X[:, np.newaxis]  

    # Back-projection
    print('Reconstructing the image from back-projection...')
    BP = BackProj(Proj, interval)  
    plt.subplot(313)
    BP = BP[20:120, 20:120]
    plt.imshow(BP)
    plt.title('Filtered Back-Projected Image')
    plt.show()
