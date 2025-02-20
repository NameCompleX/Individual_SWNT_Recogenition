import os
import numpy as np
from PIL import Image, ImageDraw
from skimage import util
from scipy.ndimage import gaussian_filter

# 设置文件夹路径
base_path = 'F:/B208/DeepLearning_assists/Figure2/pixel_resolution/input'
output_folder = os.path.join(base_path, 'lines_gap_{i}')

# 定义像素间距
pixel_gaps = [gap / 3600 for gap in range(11, 41)]

# 设置图像大小和线条参数
img_size = 360
background_color = 0  # 黑色背景
line_color = 255      # 白色线条
line_width = 1

# 遍历 pixel_gaps 生成 label 图像
for i, pixel_gap in enumerate(pixel_gaps, start=1):
    # 创建新图像
    img = Image.new('L', (img_size, img_size), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # 第一条线段
    draw.line([(img_size * (0.5 - pixel_gap), img_size * 0.2),
               (img_size * (0.5 - pixel_gap), img_size * 0.8)], 
              fill=line_color, width=line_width)

    # 第二条线段
    draw.line([(img_size * (0.5 + pixel_gap), img_size * 0.2),
               (img_size * (0.5 + pixel_gap), img_size * 0.8)], 
              fill=line_color, width=line_width)
    
    # 创建输出文件夹
    gap_folder = output_folder.format(i=i)
    os.makedirs(gap_folder, exist_ok=True)
    
    # 保存 label 图像
    label_path = os.path.join(gap_folder, 'label.png')
    img.save(label_path)
    print(f"Label 图像已保存至: {label_path}")

# 设置高斯模糊和噪音强度范围

sigma_levels = [sigma / 25 for sigma in range(15, 61)]

noise_levels = np.linspace(0.0000, 0.004, 20)  # 噪声强度

# 遍历 pixel_gaps 再次读取 label 图像，并生成 raw 图像
for i in range(1, len(pixel_gaps) + 1):
    gap_folder = output_folder.format(i=i)
    binary_image_path = os.path.join(gap_folder, 'label.png')
    
    if not os.path.exists(binary_image_path):
        print(f"未找到二值图像: {binary_image_path}")
        continue

    # 读取 label 图像
    binary_image = np.array(Image.open(binary_image_path).convert('L'))
    binary_image = (binary_image > 254).astype(float)  # 转换为二值图像

    for sigma in sigma_levels:
        # 对图像应用高斯模糊
        blurred_img = gaussian_filter(binary_image, sigma=sigma)

        for j, noise_level in enumerate(noise_levels, start=1):
            # 添加随机噪声
            noisy_image = util.random_noise(blurred_img, mode='gaussian', var=noise_level)

            # 转换为 uint8 格式
            noisy_image_uint8 = (noisy_image * 255).astype(np.uint8)

            # 保存 raw 图像
            raw_path = os.path.join(gap_folder, f'raw_sigma_{sigma}_noise_{j}.png')
            Image.fromarray(noisy_image_uint8).save(raw_path)
            print(f'Raw 图像已保存至: {raw_path}')
