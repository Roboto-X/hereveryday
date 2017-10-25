# coding:utf-8
import logging

logger = logging.getLogger("django")  # 为loggers中定义的名称


def convert_readable_img(imgsrc):
    return imgsrc.replace("blog", "")
