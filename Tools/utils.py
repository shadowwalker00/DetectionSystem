from PIL import Image
from PyQt5 import QtGui
class Utils:
    def __init__(self):
        pass
    def openImage(self,filename):
        """
        用PIL打开一张图片并返回，主要目的是封装一下PIL操作
        filename:是打开图片的本地路径
        :return:
        """
        imgPIL = Image.open(filename)
        return imgPIL

    def pil2pixmap(self,im):
        """
        将PIL图像转化成QPixmap格式的图片
        :param im:
        :return:
        """
        if im.mode == "RGB":
            pass
        elif im.mode == "L":
            im = im.convert("RGBA")
        data = im.convert("RGBA").tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)

        return pixmap

    def zoomPic(self,im,scale):
        """
        对PIL图像进行缩放
        :param im: PIl图像
        :param scale: scale是缩放的尺度
        :return: 返回缩放后的图像
        """
        return im.resize(scale)
