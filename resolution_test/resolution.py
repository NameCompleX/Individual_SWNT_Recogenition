import os
import numpy as np
from PIL import Image, ImageDraw
from skimage import util
from scipy.ndimage import gaussian_filter

# path
base_path = 'F:/B208/DeepLearning_assists/Figure2/pixel_resolution/input'
output_folder = os.path.join(base_path, 'lines_gap_{i}')

# Pixel gaps
pixel_gaps = [gap / 3600 for gap in range(11, 41)]

# Set parameters
img_size = 360
background_color = 0  
line_color = 255      
line_width = 1

#  generate GT images
for i, pixel_gap in enumerate(pixel_gaps, start=1):
    
    img = Image.new('L', (img_size, img_size), color=background_color)
    draw = ImageDraw.Draw(img)
    
    draw.line([(img_size * (0.5 - pixel_gap), img_size * 0.2),
               (img_size * (0.5 - pixel_gap), img_size * 0.8)], 
              fill=line_color, width=line_width)
    
    draw.line([(img_size * (0.5 + pixel_gap), img_size * 0.2),
               (img_size * (0.5 + pixel_gap), img_size * 0.8)], 
              fill=line_color, width=line_width)
    
    # output folder
    gap_folder = output_folder.format(i=i)
    os.makedirs(gap_folder, exist_ok=True)
    
    # save images
    label_path = os.path.join(gap_folder, 'label.png')
    img.save(label_path)
    print(f"Label has saved to {label_path}")

# Set noise and Gaussian blur parameters

sigma_levels = [sigma / 25 for sigma in range(15, 61)]

noise_levels = np.linspace(0.0000, 0.004, 20)  # noise

# generate raw images
for i in range(1, len(pixel_gaps) + 1):
    gap_folder = output_folder.format(i=i)
    binary_image_path = os.path.join(gap_folder, 'label.png')
    
    if not os.path.exists(binary_image_path):
        print(f"can not find: {binary_image_path}")
        continue

    # read label 
    binary_image = np.array(Image.open(binary_image_path).convert('L'))
    binary_image = (binary_image > 254).astype(float)  

    for sigma in sigma_levels:
        # gaussian blur
        blurred_img = gaussian_filter(binary_image, sigma=sigma)

        for j, noise_level in enumerate(noise_levels, start=1):
            # add random noise
            noisy_image = util.random_noise(blurred_img, mode='gaussian', var=noise_level)

            # change to unit8
            noisy_image_uint8 = (noisy_image * 255).astype(np.uint8)

            # save raw images
            raw_path = os.path.join(gap_folder, f'raw_sigma_{sigma}_noise_{j}.png')
            Image.fromarray(noisy_image_uint8).save(raw_path)
            print(f'Raw has saved: {raw_path}')
