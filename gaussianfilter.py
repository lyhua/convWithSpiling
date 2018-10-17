import cv2
import numpy as np
from skimage import io
from scipy import ndimage
import scipy.misc
import os

# TODO 感觉不应该保存图片，直接用卷积后的数据传递给神经网络

# 拉普拉斯 卷积核
kernel_3x3 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])


def create_gaussianBlur(image_path, save_path, image_name, format):
    '''

    :param image_path: 要处理图片的绝对路径
    :param save_path: 处理图片的保存路径
    :param image_name: 保存图片的名称
    :param format: 保存图片的格式
    :return:
    '''

    # 不同卷积的文件夹
    kernel3 = "3x3"
    kernel5 = "5x5"
    # 不同卷积图片的名称
    k3_image_name = image_name + "_" + kernel3 + "." + format
    k5_image_name = image_name + "_" + kernel5 + "." + format
    # 创建不同卷积核图片文件夹相对路径
    k3_relativepath = os.path.join(save_path, kernel3)
    k5_relativepath = os.path.join(save_path, kernel5)
    # 判断文件夹是否存在
    if(os.path.exists(k3_relativepath) is False):
        os.makedirs(k3_relativepath)
    if(os.path.exists(k5_relativepath) is False):
        os.makedirs(k5_relativepath)
    # 图片保存的绝对路径
    k3path = os.path.join(k3_relativepath, k3_image_name)
    k5path = os.path.join(k5_relativepath, k5_image_name)
    # print("k3path:", k3path)
    # print("k5path:", k5path)
    # 读取图片
    img = io.imread(image_path, as_gray=True)
    # 分别用不同卷积核进行卷积
    k3 = ndimage.convolve(img, kernel_3x3)
    k5 = ndimage.convolve(img, kernel_5x5)
    # 保存不同卷积图片
    scipy.misc.imsave(k3path, k3)
    scipy.misc.imsave(k5path, k5)


if __name__ == "__main__":
    path = "H:/netdata/spiling1/4cam_splc/canong3_canonxt_sub_01.tif"
    savepath = "H:/netdata/shiyan"
    create_gaussianBlur(image_path=path, save_path=savepath, image_name="canong3_canonxt_sub_01", format="tif")



