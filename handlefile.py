import os
from gaussianfilter import *
from scipy import ndimage
from scipy import misc
import cv2
import copy


def get_FileList(dir):
    '''
    获取文件列表
    :param dir: 文件的绝对路径
    :return: 文件列表绝对路径
    '''
    file_list = []
    name_list = []
    format_list = []
    for s in os.listdir(dir):
        names = s.split(".")
        newDir = os.path.join(dir, s)
        file_list.append(newDir)
        name_list.append(names[0])
        format_list.append(names[1])
    return file_list, name_list, format_list

def change_image_with_gaussianfilter(dir, save_path, format):
    '''
    将给定文件夹中的所有图片进行卷积处理
    :param dir: 图片所在的文件夹
    :param save_path: 保存图片的路径
    :param format: 保存图片的格式
    :return:
    '''
    # 判断保存图片文件夹是否存在
    if(os.path.exists(save_path) is False):
        # 不存在就创建文件夹
        os.makedirs(save_path)

    # 获取文件夹中的所有文件名
    imagepaths, names, _ = get_FileList(dir)
    for (path,name) in zip(imagepaths, names):
        create_gaussianBlur(path, save_path, name, format)


def rotate_image_with_angle(dir, save_path, angle):
    '''
    用于旋转图片
    :param dir: 被旋转图片所在的文件夹
    :param save_path: 旋转图片保存的文件夹
    :param angle: 旋转角度(这里实验取 90， 180 ，270)
    :return:
    '''
    # 根据旋转角度创建文件夹
    real_save_path = os.path.join(save_path, str(angle))
    # 判断图片保存的文件是否存在
    if(os.path.exists(real_save_path) is False):
        os.makedirs(real_save_path)
    # 获取文件夹中的所有文件名
    imagepaths, names, formats = get_FileList(dir)
    for (path, name, format) in zip(imagepaths, names, formats):
        image = misc.imread(path)
        # 进行图片旋转
        img_rote = ndimage.rotate(image, angle)
        # 把图片的扩展加上和旋转角度
        image_name = name + "_" + str(angle) + "." + format
        # 创建旋转图片的绝对路径
        real_path = os.path.join(real_save_path, image_name)
        # print(real_path)
        # 保存图片
        misc.imsave(real_path, img_rote)

def mirror_imgs(image_path, save_path, name, format, mode):
    '''
    用于对图片进行镜像变化
    :param image_path: 处理图片的路径
    :param save_path: 保存图片路径
    :param name: 图片名称
    :param format: 图片的格式
    :param mode: iLR:水平镜像 iUD垂直镜像 iAcross:对角镜像
    :return:
    '''
    image_name = name + "_" + str(mode) + "."  + format
    image_real_path = os.path.join(save_path, image_name)
    print("image_real_path: " + image_real_path)
    image = cv2.imread(image_path, 1)
    height = image.shape[0]
    width = image.shape[1]
    if mode == "iLR":
        iLR = copy.deepcopy(image)
        for i in range(height):
            for j in range(width):
                iLR[i, width - 1 - j] = image[i, j]
        cv2.imwrite(image_real_path, iLR)

    if mode == "iUD":
        iUD = copy.deepcopy(image)
        for i in range(height):
            for j in range(width):
                iUD[height - i - 1, j] = image[i, j]
        cv2.imwrite(image_real_path, iUD)

    if mode == "iAcross":
        iAcross = copy.deepcopy(image)
        for i in range(height):
            for j in range(width):
                iAcross[height - i - 1, width - j - 1] = image[i, j]
        cv2.imwrite(image_real_path, iAcross)

def mirror_imgs_with_mode(dir, save_path, mode="iLR"):
    '''
    对一个文件夹中的图片进行镜像操作
    :param dir: 被操作图片所在的文件夹
    :param save_path: 操作后保存图片的路径
    :param mode: 进行镜像操作类型 iLR:水平镜像 iUD垂直镜像 iAcross:对角镜像
    :return:
    '''
    save_real_path = os.path.join(save_path, str(mode))
    # 判断保存图片文件夹是否存在
    if os.path.exists(save_real_path) is False:
        os.makedirs(save_real_path)
    # 获取文件夹中的所有文件名
    imagepaths, names, formats = get_FileList(dir)
    # 对图片进行镜像操作
    for (path, name, format) in zip(imagepaths, names, formats):
        mirror_imgs(path, save_real_path, name, format, mode)


if __name__ == "__main__":
    path = "H:/netdata/shiyan/test"
    save_path = "H:/netdata/shiyan"
    mirror_imgs_with_mode(path, save_path, mode="iLR")
    # rotate_image_with_angle(path, save_path, 90)

