# 碳纳米管SEM图像去卷积与表征

## 项目简介

本项目旨在通过对碳纳米管的扫描电子显微镜（SEM）图像进行去卷积，获得碳纳米管的精准位置，以进一步计算取向分布和密度表征。
由于真实SEM图像中碳纳米管的真实位置难以获得，本项目采用生成数据集的方法进行模型训练。

## 数据集生成

- **Generate_array.ipynb**：用于生成阵列取向的碳纳米管数据集
- **Generate_random.ipynb**：用于生成随机取向的碳纳米管数据集

## 模型训练与测试

- **Train.ipynb**：用于训练模型
- **Test.ipynb**：用于测试模型

## 演示数据

- **GT_demo/**：包含示例的真实位置（Ground Truth）数据
- **input_demo/**：包含示例的输入SEM图像

## 分辨率测试

- **resolution_test/**：用于模型分辨率性能测试的实验结果和相关数据

---

# CNT SEM Image Deconvolution and Characterization

## Project Overview

This project aims to deconvolve scanning electron microscope (SEM) images of carbon nanotubes (CNTs) to extract their precise positions, which are then used for orientation distribution calculation and density characterization.
Since the true positions of CNTs in real SEM images are difficult to obtain, synthetic datasets are generated for model training.

## Dataset Generation

- **Generate_array.ipynb**: Generates datasets of array-oriented CNTs
- **Generate_random.ipynb**: Generates datasets of randomly oriented CNTs

## Model Training and Testing

- **Train.ipynb**: Used for training the model
- **Test.ipynb**: Used for testing the model

## Environment Dependencies

- **requirements.txt**: Lists all required dependencies

## Demo Data

- **GT_demo/**: Example ground truth data
- **input_demo/**: Example SEM input images

## Resolution Test

- **resolution_test/**: Contains experiments and results for model resolution performance testing
